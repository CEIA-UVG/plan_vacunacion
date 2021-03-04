"""
============
vacunados.py
============

Clase encargada de leer y mantener los datos acerca de los pacientes ya vacunados. Consta de una clase llamada
:class:`~vacunados.Vacunado` que guarda todos los valores relevantes a los pacientes, y el método
:func:`~vacunados.readVacunados` que lee los datos del archivo con la información de los pacientes y los graba en una
instancia de la clase Vacunado.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores acerca
de las pacientes vacunados.
"""
import pandas as pd
import datetime


class Vacunado:
    """
    Guarda la información de un paciente vacunado:
    * Código del paciente
    * Clínica de vacunación
    * Fecha de Vacunación
    * Vacuna utilizada
    """
    def __init__(self, codigo, clinica, fecha, vacuna):
        self.codigo = codigo
        self.clinica = clinica
        self.fecha = fecha
        self.vacuna = vacuna

    def getCodigo(self):
        """
        :return: El codigo del paciente vacunado
        :rtype: String
        """
        return self.codigo

    def getClinica(self):
        """
        :return: El codigo de la clínica donde el paciente fue vacunado
        :rtype: String
        """
        return self.clinica

    def getFecha(self):
        """
        :return: La fecha cuando el paciente fue vacunado.
        :rtype: Datetime
        """
        return self.fecha

    def getVacuna(self):
        """
        :return: El codigo de la vacuna utilizada
        :rtype: int
        """
        return self.vacuna


def readVacunados(fn, verbose=False, debug=False):
    """
    Lee la información de los pacientes vacunados disponible en el archivo *fn* y la guarda en un objeto
    tipo :class:`~vacunados.Vacunado`.

    :param fn: Ubicación del archivo con la información de los pacientes vacunados.
    :type fn: String
    :param verbose: Opcional. Si es verdadero muestra información adicional al correrse.
    :type verbose: Boolean
    :param debug: Opcional. Si es verdadero muestra información útil para la depuración.
    :type debug: Boolean
    :return: Lista de pacientes vacunados con las variables leidas del archivo.
    :rtype: list
    """
    df = pd.read_csv(fn, encoding="latin")
    resultados = []
    i = 0
    for row in df.iterrows():
        i += 1
        v = Vacunado(row[1]['codigo'], row[1]['clinica'], datetime.datetime.strptime(row[1]['fecha'], "%d/%m/%Y"),
                     row[1]['vacuna'])
        resultados.append(v)
    if verbose:
        print('Leidos ' + str(i) + ' vacunados...')
    return resultados
