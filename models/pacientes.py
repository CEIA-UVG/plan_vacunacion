"""
============
pacientes.py
============

Clase encargada de leer y mantener los datos acerca de los pacientes. Consta de una clase llamada
:class:`~pacientes.Paciente` que guarda todos los valores relevantes a los pacientes, y el método
:func:`~pacientes.readPacientes` que lee los datos del archivo con la información de los pacientes y los graba en una
instancia de la clase Paciente.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores acerca
de las pacientes.
"""
import pandas as pd
from helper import readPriorityEdad, readPriorityUnidades, readPriorityMunicipios, readPriorityCargos


class Paciente:
    """
    Guarda la información de un paciente:
    * Codigo del paciente.
    * NIT del paciente.
    * Nombre del paciente.
    * Sexo del Paciente.
    * Número de afiliado.
    * Fecha de Nacimiento.
    * Edad del paciente.
    * Renglon de contratación del paciente si disponible.
    * Cargo del paciente.
    * Número de empleado del paciente si disponible.
    * Departamento donde el paciente habita.
    * Municipio donde el paciente habita.
    * Zona donde el paciente habita.
    * Dirección donde el paciente habita.
    * Nombre de la dependencia donde trabaja.
    * Departamento de la dependencia donde trabaja.
    * Municipio de la dependencia donde trabaja.
    * Código de la unidad de vacunación.
    * Fase a la que el paciente pertenece.
    * Subfase a la que el paciente pertenece.
    * Si el paciente ha tenido COVID-19.
    * Si el paciente tiene diabetes miellitus.
    * Si el paciente tiene sobrepeso.
    * Si el paciente ha tenido cancer.
    * Si el paciente es VIH Positivo.
    * Si el paciente tiene enfermedad renal.
    * La prioridad respecto a su edad.
    * La prioridad respecto a su cargo.
    * La prioridad respecto al lugar donde habita.
    * La prioridad respecto al lugar donde trabaja.
    """
    def __init__(self, codigo, nit, nombre, sexo, numafiliado, fdn,
                 edad, renglon, cargo, numempleado,
                 deptohabita, munihabita, zonahabita, direccion,
                 nombredependencia, deptodependencia, munidependencia,
                 codigounidadadscripcion, fase, subfase, covid,
                 diabetes, sobrepeso, cancer, vih, renal, priorityedad, prioritycargo,
                 priorityhabita, prioritydependencia, params):
        self.codigo = codigo
        self.nit = nit
        self.nombre = nombre
        self.sexo = sexo
        self.numAfiliado = numafiliado
        self.fdn = fdn
        self.edad = edad
        self.renglon = renglon
        self.cargo = cargo
        self.numEmpleado = numempleado
        self.deptoHabita = deptohabita
        self.muniHabita = munihabita
        self.zonaHabita = zonahabita
        self.direccion = direccion
        self.nombreDependencia = nombredependencia
        self.deptoDependencia = deptodependencia
        self.muniDependencia = munidependencia
        self.codigoUnidadAdscripcion = codigounidadadscripcion
        self.fase = fase
        self.subfase = subfase
        if params.getPesoCovid() > 0 and covid != -1:
            self.covid = covid / params.getPesoCovid()
        else:
            self.covid = 2
        if params.getPesoDiabetes() > 0 and diabetes != -1:
            self.diabetes = diabetes / params.getPesoDiabetes()
        else:
            self.diabetes = 2
        if params.getPesoPeso() > 0 and sobrepeso != -1:
            self.sobrepeso = sobrepeso / params.getPesoPeso()
        else:
            self.sobrepeso = 2
        if params.getPesoCancer() > 0 and cancer != -1:
            self.cancer = cancer / params.getPesoCancer()
        else:
            self.cancer = 2
        if params.getPesoVih() > 0 and vih != -1:
            self.vih = vih / params.getPesoVih()
        else:
            self.vih = 2
        if params.getPesoRenal() > 0 and renal != -1:
            self.renal = renal / params.getPesoRenal()
        else:
            self.renal = 2
        if params.getPesoEdad() > 0 and priorityedad != -1:
            self.priorityEdad = priorityedad / params.getPesoEdad()
        else:
            self.priorityEdad = 10
        if params.getPesoCargo() > 0 and prioritycargo != -1:
            self.priorityCargo = prioritycargo / params.getPesoCargo()
        else:
            self.priorityCargo = 10
        if params.getPesoHabita() > 0 and priorityhabita != -1:
            self.priorityHabita = priorityhabita / params.getPesoHabita()
        else:
            self.priorityHabita = 10
        if params.getPesoTrabaja() > 0 and prioritydependencia != -1:
            self.priorityDependencia = prioritydependencia / params.getPesoTrabaja()
        else:
            self.priorityDependencia = 10
        self.priority = 0
        if self.priorityEdad > 0:
            self.priority += self.priorityEdad
        if self.priorityCargo > 0:
            self.priority += self.priorityEdad
        if self.priorityHabita > 0:
            self.priority += self.priorityEdad
        if self.priorityDependencia > 0:
            self.priority += self.priorityEdad
        if self.covid > 0:
            self.priority += self.priorityEdad
        if self.diabetes > 0:
            self.priority += self.priorityEdad
        if self.sobrepeso > 0:
            self.priority += self.priorityEdad
        if self.cancer > 0:
            self.priority += self.priorityEdad

    def getPrioridad(self):
        """
        :return: La prioridad en la que la persona debe ser vacunada (entre menor sea el numero mayor prioridad).
        :rtype: int
        """
        return self.priority

    def getCodigo(self):
        """
        :return: El código de identificación del paciente.
        :rtype: String
        """
        return self.codigo

    def __str__(self):
        return self.codigo + "," + self.nombre + "," + str(self.edad)


def readPacientes(fn, params, verbose=False, debug=False):
    """
    Lee la información de los pacientes disponible en el archivo *fn* y la guarda en un objeto tipo
    :class:`~pacientes.Paciente`.

    :param fn: Ubicación del archivo con la información de los pacientes.
    :type fn: String
    :para params: Parametros de la configuracion
    :type params: ConfigParams
    :param verbose: Opcional. Si es verdadero muestra información adicional al correrse.
    :type verbose: Boolean
    :param debug: Opcional. Si es verdadero muestra información útil para la depuración.
    :type debug: Boolean
    :return: Lista de Pacientes con las variables leidas del archivo.
    :rtype: list
    """
    df = pd.read_csv(fn, encoding="latin")

    priorityEdades = readPriorityEdad(params.getPathToFiles()+params.getFileEdad())
    priorityCargos = readPriorityCargos(params.getPathToFiles()+params.getFileCargos())
    priorityUnidades = readPriorityUnidades(params.getPathToFiles()+params.getFileUnidades())
    priorityMunicipios = readPriorityMunicipios(params.getPathToFiles()+params.getFileMuni())

    result = {}
    for row in df.iterrows():
        codigo = row[1]['codigo']
        nit = row[1]['nit']
        nombre = row[1]['nombre']
        sexo = row[1]['sexo']
        num_afiliado = row[1]['numafiliado']
        fdn = row[1]['fdn']
        edad = int(row[1]['edad'])
        renglon = row[1]['renglon']
        cargo = row[1]['cargo']
        num_empleado = row[1]['numempleado']
        codigo_habita = row[1]['codigoHabita']
        depto_habita = row[1]['departamento']
        muni_habita = row[1]['municipio']
        zona_habita = row[1]['zona']
        direccion = row[1]['direccion']
        nombre_dependencia = row[1]['nombredependencia']
        depto_dependencia = row[1]['departamentoDependencia']
        muni_dependencia = row[1]['municipioDependencia']
        codigo_unidad_adscripcion = row[1]['nombreUnidadAdscripcion']
        fase = row[1]['Fase']
        subfase = row[1]['SubFase']
        covid = 1 if row[1]['tuvoCovid'] == "Si" else 0
        diabetes = 1 if row[1]['diabetico'] == "Si" else 0
        sobrepeso = 1 if row[1]['sobrepeso'] == "Si" else 0
        cancer = 1 if row[1]['cancer'] == "Si" else 0
        vih = 1 if row[1]['VIH'] == "Si" else 0
        renal = 1 if row[1]['Renal'] == "Si" else 0
        if edad - edad % 10 in priorityEdades:
            priority_edad = priorityEdades[edad - edad % 10]
        else:
            if debug:
                print("Advertencia: El paciente "+str(codigo)+" no tiene una edad valida.")
            priority_edad = 5
        if cargo in priorityCargos:
            priority_cargo = priorityCargos[cargo]
        else:
            if debug:
                print("Advertencia: El paciente " + str(codigo) + " no tiene un cargo valido.")
            priority_cargo = 4
        if str(depto_habita)+", "+str(muni_habita) in priorityMunicipios:
            priority_habita = priorityMunicipios[str(depto_habita)+", "+str(muni_habita)]
        else:
            if debug:
                print("Advertencia: Paciente " + str(codigo) + " no tiene un departamento y municipio valido.")
            priority_habita = 2
        if codigo_unidad_adscripcion in priorityUnidades:
            priority_dependencia = priorityUnidades[codigo_unidad_adscripcion]
        else:
            if debug:
                print("Advertencia: El paciente " + str(codigo) + " no tiene una unidad valida")
            priority_dependencia = 5
        p = Paciente(codigo, nit, nombre, sexo, num_afiliado, fdn, edad, renglon,
                     cargo, num_empleado, depto_habita, muni_habita,
                     zona_habita, direccion, nombre_dependencia, depto_dependencia,
                     muni_dependencia, codigo_unidad_adscripcion, fase, subfase,
                     covid, diabetes, sobrepeso, cancer, vih, renal, priority_edad,
                     priority_cargo, priority_habita, priority_dependencia, params)
        if codigo_unidad_adscripcion not in result:
            result[codigo_unidad_adscripcion] = []
        result[codigo_unidad_adscripcion].append(p)

    for k in result.keys():
        result[k].sort(key=lambda x: x.priority)

    if verbose or debug:
        print('Leidos ' + str(len(result)) + ' pacientes...')

    return result
