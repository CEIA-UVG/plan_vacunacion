# -*- coding: utf-8 -*-
"""
============================
Programa Principal (main.py)
============================

:Authors:
    Juan F. Mancilla-Caceres,
    Lynette Garcia,
    Luis Furlan

:Version: 0.9 beta

Programa para generar orden de distribución de vacunas (originalmente para COVID-19) realizdo por el Centro de
Estudios en Informática Aplicada (CEIA) de la Universidad del Valle de Guatemala (UVG).

Parametros de uso
-----------------

-v  Si se encuentra presente, el programa desplegará información adicional durante su corrida.
-d  Si se encuentra presente, el programa desplegará información útil para depurar el programa.
-u  Si se encuentra preselte, el programa calcula la segunda dosis de vacunas según las personas vacunadas.

Archivos necesarios de entrada:
-------------------------------

- config.txt: Archivo con información necesaria para correr el programa.
- clinicas.csv: Archivo con información de las clínicas.
- pacientes.csv: Archivo con información de cada uno de los pacientes a vacunar.
- lote_vacunas.csv: Archivo con información acerca de los lotes de vacunas.
- prioridadCargos.csv: Archivo con información acerca de la prioridad respecto a cargos.
- prioridadEdad.csv: Archivo con información acerca de la prioridad respecto a edad.
- prioridadMunicipios.csv: Archivo con información acerca de la prioridad respecto a municipios.
- prioridadUnidades.csv: Archivo con información acerca de la prioridad respecto a unidades.
- vacunas.csv: Archivo con información acerca de cada vacuna a aplicar.
- excluir.csv: Archivo con información acerca de pacientes a excluir de la vacunación.
- vacunados.csv: Archivo con información acerca de que pacientes realmente fueron vacunados.

Archivo de salida:
------------------

- asignaciones.csv conteo de personas por centro y fase a la que pertenecen con fecha de vacunación con prioridad.
- asignaciones_reales_dosis_2.csv asignación de segunda dosis en función de las personas que fueron realmente vacunadas.

"""
import datetime
import sys
import getopt

from models.asignaciones import Asignacion
from models.clinicas import readClinicas
from models.config import readConfig
from helper import getAppropriatedate, excluirPaciente
from models.lotes import readLotes
from models.pacientes import readPacientes
from models.vacunas import readVacunas
from models.excluidos import readExcluidos
from models.vacunados import readVacunados

params = None


def areWeDone(d):
    """
    Calcula cuantas vacunas faltan por asignar, si es 0 retorna verdadero, sino falso.
    :param d: Diccionario con llave clinica y valor numero de vacunas que faltan por asignar
    :type d: dict
    :return: Verdadero si ya no hay mas vacunas a agregar, Falso sino.
    :rtype: bool
    """
    n = 0
    for k in d.keys():
        n += d[k]
    if n > 0:
        return False
    return True


def computeAsignaciones(lotes, lista_de_clinicas, remaining_vaccines_per_clinic, pacientes, vacunas_por_dia_por_clinica,
                        lista_de_vacunas, fase, excluidos):
    asignaciones = []
    for lote in lotes:
        num_vaccines_for_first_dose = lote.getRondas()
        tiempo_entre_dosis = lista_de_vacunas[lote.getMarca()].getTiempo()
        while num_vaccines_for_first_dose > 1:
            for clinica in lista_de_clinicas:
                left = remaining_vaccines_per_clinic[clinica.getCodigo()]
                if left > 0:
                    # Obtenemos el siguiente paciente para esta clinica
                    num_patient = pacientes[clinica.getCodigo()].pop(0).getCodigo()
                    # Si el paciente esta en la lista de excluidos lo ignoramos y sacamos el siguiente
                    while excluirPaciente(num_patient, excluidos):
                        num_patient = pacientes[clinica.getCodigo()].pop(0).getCodigo()
                    # Calculamos el orden relativo a esta clinica del paciente
                    orden = clinica.getMaxPerPhase(fase) - left + 1
                    # Calculamos la fecha de la primera dosis para este paciente en funcion de cuando se recibieron
                    # las vacunas y a cuantas personas ya hemos vacunado
                    fecha_applicacion_dosis1 = lote.getFecha() + datetime.timedelta(days=clinica.getTiempo())
                    fecha1 = getAppropriatedate(clinica.getCodigo(), vacunas_por_dia_por_clinica,
                                                fecha_applicacion_dosis1, params, clinica.getCapacidad())
                    # Calculamos la fecha de la segunda dosis tomando en cuenta el tiempo entre dosis
                    fecha_applicacion_dosis2 = lote.getFecha() + datetime. \
                        timedelta(days=clinica.getTiempo()) + datetime.timedelta(weeks=tiempo_entre_dosis)
                    fecha2 = getAppropriatedate(clinica.getCodigo(), vacunas_por_dia_por_clinica,
                                                fecha_applicacion_dosis2, params, clinica.getCapacidad())
                    # Anotamos cuantas vacunas van en el dia de aplicacion
                    if fecha1 not in vacunas_por_dia_por_clinica[clinica.getCodigo()]:
                        vacunas_por_dia_por_clinica[clinica.getCodigo()][fecha1] = 0
                    if fecha2 not in vacunas_por_dia_por_clinica[clinica.getCodigo()]:
                        vacunas_por_dia_por_clinica[clinica.getCodigo()][fecha2] = 0
                    vacunas_por_dia_por_clinica[clinica.getCodigo()][fecha1] += 1
                    vacunas_por_dia_por_clinica[clinica.getCodigo()][fecha2] += 1
                    # Creamos las asignaciones para ambas dosis
                    asignacion_dosis1 = Asignacion(str(num_patient), lote.getMarca(), 1, clinica.getCodigo(), orden,
                                                   fecha1)
                    asignacion_dosis2 = Asignacion(str(num_patient), lote.getMarca(), 2, clinica.getCodigo(), orden,
                                                   fecha2)
                    asignaciones.append(asignacion_dosis1)
                    asignaciones.append(asignacion_dosis2)
                    # reducimos el numero de vacunas y el numero de vacunas que tocan por clinica
                    remaining_vaccines_per_clinic[clinica.getCodigo()] -= 1
                    num_vaccines_for_first_dose -= 1
            if areWeDone(remaining_vaccines_per_clinic):
                break
    return asignaciones


def runInitialAssignment(verbose, debug):
    """
    Si el programa se corre sin el parametro -u, calcula la distribución de vacunas a utilizar por clínica y paciente.
    Utiliza los datos de la disponibilidad de los lotes de vacunas, la lista de pacientes, sus datos personales, y
    las capacidades de las clínicas para asignar ambas dosis.
    :param verbose: Si es True despliega información adicional mientras corre.
    :type verbose: bool
    :param debug: Si es True despliega información util para la depuración.
    :type debug: bool
    """
    if verbose:
        print("Usando " + str(params.getNumEstacionesPorDepencencia()) + " estaciones por dependencia.")
        print("")

    # Lee las clinicas, vacunas y lotes de vacunas
    lista_de_clinicas = readClinicas(params.getPathToFiles()+params.getFileClinicas(), verbose, debug)
    lista_de_vacunas = readVacunas(params.getPathToFiles()+params.getFileVacunas(), verbose, debug)
    lotes = readLotes(params.getPathToFiles()+params.getFileLotes(), verbose, debug)

    if verbose:
        print("Leyendo pacientes...")
    pacientes = readPacientes(params.getPathToFiles()+params.getFilePacientes(), params, verbose, debug)

    # Ordena los lotes en orden ascendente de fecha para asignar primero las vacunas que se reciben antes.
    for lote in lotes:
        tipo_vacuna = lote.getMarca()
        num_dosis = lista_de_vacunas[tipo_vacuna].getDosis()
        lote.setRondas(lote.getNum() // num_dosis)

    if verbose:
        print("Ordenando lotes...")
    # find first lote
    lotes.sort(key=lambda x: x.ingreso)

    if verbose:
        print("Leyendo pacientes a excluir de la vacuna...")
    excluidos = readExcluidos(params.getPathToFiles()+params.getFileExcluidos(), verbose, debug)

    # Por cada fase, asignamos las vacunas en orden
    fases = ['n1a', 'n1b', 'n1c', 'n2a', 'n2b', 'n2c', 'n2d', 'n3a', 'n4a', 'n4b', 'n4c', 'n4d']
    asignaciones = []

    for fase in fases:
        if verbose:
            print("Calculando vacunas de la fase " + fase + " por clínica...")
        # compute how many vaccines per clinic (start with capacity)
        remaining_vaccines_per_clinic = {}
        vacunas_por_dia_por_clinica = {}
        for clinica in lista_de_clinicas:
            remaining_vaccines_per_clinic[clinica.getCodigo()] = clinica.getMaxPerPhase(fase)
            vacunas_por_dia_por_clinica[clinica.getCodigo()] = {}

        # start applying first lot, 1 vaccine per clinic, unless the clinic is at its full.
        if verbose:
            print("Asignando vacunas para la fase " + fase + "...")
        asignaciones += computeAsignaciones(lotes, lista_de_clinicas, remaining_vaccines_per_clinic, pacientes,
                                           vacunas_por_dia_por_clinica, lista_de_vacunas, fase, excluidos)

    # Imprimimos los resultados
    if verbose:
        print("Imprimiendo resultado...")
    asignaciones.sort(key=lambda x: [x.dependencia, x.fecha, x.dosis, x.orden])
    f = open(params.getPathToFiles()+'asignaciones.csv', 'w')
    f.write("IdPaciente,codigoDependencia,tipo_vacuna,Dosis,orden,fecha\n")
    for a in asignaciones:
        f.write(str(a))
        f.write("\n")
    f.close()
    print("\nListo.")


def runUpdate(verbose, debug):
    """
    Si el programa se corre con el parametro -u, lee la lista de personas que fueron vacunadas en la realidad (las
    cuales pueden ser distintas a las generadas originalmente) y calcula cuando deben recibir la segunda dosis.
    """
    # Lee las vacunas e información de personas vacunadas.
    lista_de_vacunas = readVacunas(params.getPathToFiles() + params.getFileVacunas(), verbose, debug)

    vacunados = readVacunados(params.getPathToFiles()+params.getFileVacunados(), verbose, debug)
    asignaciones = []
    orden = 0

    # En función de las personas vacunadas, se crea la asignación de la segunda dosis.
    for vacunado in vacunados:
        orden += 1
        asignacion_dosis_1 = Asignacion(vacunado.getCodigo(), vacunado.getVacuna(), 1, vacunado.getClinica(), orden,
                                                   str(vacunado.getFecha()))
        tiempo_entre_dosis = lista_de_vacunas[vacunado.getVacuna()].getTiempo()
        fecha_2 = vacunado.getFecha() + datetime.timedelta(weeks=tiempo_entre_dosis)
        asignacion_dosis_2 = Asignacion(vacunado.getCodigo(), vacunado.getVacuna(), 2, vacunado.getClinica(), orden,
                                        str(fecha_2))
        asignaciones.append(asignacion_dosis_1)
        asignaciones.append(asignacion_dosis_2)

    # Imprimimos los resultados.
    if verbose:
        print("Imprimiendo asignaciones basados en vacunaciones...")
    asignaciones.sort(key=lambda x: [x.dependencia, x.fecha, x.dosis, x.orden])
    f = open(params.getPathToFiles()+'asignaciones_reales_dosis_2.csv', 'w')
    f.write("IdPaciente,codigoDependencia,tipo_vacuna,Dosis,orden,fecha\n")
    for a in asignaciones:
        f.write(str(a))
        f.write("\n")
    f.close()
    print("\nListo.")


def main(argv):
    """
    Programa principal que recibe los parametros de entrada y ejecuta el codigo correspondiente.
    """
    verbose = True
    debug = False
    update_mode = False

    try:
        opts, args = getopt.getopt(argv, "vdu")
    except getopt.GetoptError:
        print('Argumento no reconocido')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-v':
            verbose = True
        if opt == '-d':
            debug = True
        if opt == '-u':
            update_mode = True

    if update_mode:
        runUpdate(verbose,debug)
    else:
        runInitialAssignment(verbose,debug)


if __name__ == "__main__":
    params = readConfig('config.txt')
    main(sys.argv[1:])
