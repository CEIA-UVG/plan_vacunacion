"""
===========
excluidos.py
===========

Clase encargada de leer y mantener los datos acerca de los pacientes que no serán vacunados por cualquier razón.
Contiene la clase :class:`~excluidos.Excluido` que guarda todos los valores relevantes a los pacientes, y el método
:func:`~excluidos.readExcluidos` que lee los datos del archivo con la información de los pacientes y los graba en una
instancia de la clase Excluido.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores acerca
de los pacientes a excluir.
"""
import pandas as pd


class Excluido:
    """
    Guarda la información de los pacientes a excluir de la vacuna:
    * codigo
    * razón de la exclusión
    """
    def __init__(self, codigo, razon):
        self.codigo = codigo
        self.razon = razon

    def getCodigo(self):
        """
        :return: El código de identificación del paciente a excluir
        :rtype: String
        """
        return self.codigo

    def getRazon(self):
        """
        :return: La razón para excluir al paciente
        :rtype: String
        """
        return self.razon


def readExcluidos(fn, verbose = False, debug = False):
    """
    Lee la información de los pacientes a excluir del archivo *fn* y la guarda en un objeto
    tipo :class:`~excluidos.Excluido`.

    :param fn: Ubicación del archivo con la información de los pacientes a excluir.
    :type fn: String
    :param verbose: Opcional. Si es verdadero muestra información adicional al correrse.
    :type verbose: Boolean
    :param debug: Opcional. Si es verdadero muestra información útil para la depuración.
    :type debug: Boolean
    :return: Lista de Pacientes a excluir con las variables leidas del archivo.
    :rtype: list
    """
    df = pd.read_csv(fn, encoding="latin")
    result = []
    i = 0
    for row in df.iterrows():
        i += 1
        if debug:
            print(row)
        e = Excluido(row[1]['codigo'], row[1]['razon'])
        result.append(e)
    if verbose:
        print('Leidos ' + str(i) + ' pacientes a excluir...')
    return result
