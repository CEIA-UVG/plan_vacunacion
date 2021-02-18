"""

"""
import datetime
import pandas as pd


def getAppropriatedate(clinica, vacunas_por_dia_por_clinica, fecha_de_inicio, params):
    """

    :param clinica:
    :param vacunas_por_dia_por_clinica:
    :param fecha_de_inicio:
    :param params:
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

    :param fn:
    :return:
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['edad']] = int(row[1]['prioridad'])
    return result


def readPriorityUnidades(fn):
    """

    :param fn:
    :return:
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['dependencia']] = int(row[1]['prioridad'])
    return result


def readPriorityMunicipios(fn):
    """

    :param fn:
    :return:
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['Departamento'] + ", " + row[1]['Municipio']] = int(row[1]['Prioridad'])
    return result


def readPriorityCargos(fn):
    """

    :param fn:
    :return:
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    for row in df.iterrows():
        result[row[1]['cargos']] = int(row[1]['prioridad'])
    return result
