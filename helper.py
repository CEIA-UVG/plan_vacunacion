"""
=========
helper.py
=========

Módulo con funciones de ayuda para obtener las fechas apropiadas de vacunación y las prioridades obtenidas de los
archivos de entrada.

"""
import datetime
import pandas as pd


def getAppropriatedate(clinica, vacunas_por_dia_por_clinica, fecha_de_inicio, params):
    """
    Devuelve la fecha de aplicación de una vacuna en función de cuantas vacunas se ha puesto desde el inicio de la
    campaña y en función de la capacidad de cada centro de vacunación.

    :param clinica: codigo de la clinica
    :param vacunas_por_dia_por_clinica: numero de vacunas que se aplican por dia en la clinica
    :param fecha_de_inicio: fecha de inicio de aplicaciones de la vacuna
    :param params: ConfigParams
    :return:
    """
    while True:
        if fecha_de_inicio not in vacunas_por_dia_por_clinica[clinica]:
            return fecha_de_inicio
        if vacunas_por_dia_por_clinica[clinica][fecha_de_inicio] < \
                params.getNumEstacionesPorDepencencia() * params.getNumVacunasPorEstacionPorDia():
            return fecha_de_inicio
        fecha_de_inicio = fecha_de_inicio + datetime.timedelta(days=1)


def readPriorityEdad(fn):
    """
    Devuelve un diccionario con los valores de prioridad por edad leidos del archivo *fn*
    :param fn: nombre del archivo
    :return: diccionario con prioridades
    :rtype: dict
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['edad']] = int(row[1]['prioridad'])
    return result


def readPriorityUnidades(fn):
    """
    Devuelve un diccionario con los valores de prioridad por Unidad leidos del archivo *fn*
    :param fn: nombre del archivo
    :return: diccionario con prioridades
    :rtype: dict
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['dependencia']] = int(row[1]['prioridad'])
    return result


def readPriorityMunicipios(fn):
    """
    Devuelve un diccionario con los valores de prioridad por municipio leidos del archivo *fn*
    :param fn: nombre del archivo
    :return: diccionario con prioridades
    :rtype: dict
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['Departamento'] + ", " + row[1]['Municipio']] = int(row[1]['Prioridad'])
    return result


def readPriorityCargos(fn):
    """
    Devuelve un diccionario con los valores de prioridad por cargo leidos del archivo *fn*
    :param fn: nombre del archivo
    :return: diccionario con prioridades
    :rtype: dict
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['cargos']] = int(row[1]['prioridad'])
    return result
