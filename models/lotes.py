"""
=========
lotes.py
=========

Clase encargada de leer y mantener los datos acerca de los lotes de vacunas. Consta de una clase llamada
:class:`~lotes.Lote` que guarda todos los valores relevantes a los lotes de vacunas, y el método
:func:`~lotes.readLotes` que lee los datos del archivo con la información de los lotes y los graba en una instancia
de la clase Lote.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores acerca
de los lotes de vacunas.
"""
import datetime
import pandas as pd


class Lote:
    """
    Guarda la información de un lote: id, fecha de ingreso, marca, cantidad y el número de aplicaciones disponibles.
    """
    def __init__(self):
        self.id = ""
        self.ingreso = ""
        self.marca = -1
        self.n = -1
        self.rondas = -1

    def __str__(self):
        return str(self.marca) + "\t" + str(self.n)

    def setId(self, i):
        """
        :param i: El codigo de identificación del lote
        :type i: String
        :return: None
        """
        self.id = i

    def setIngreso(self, ing):
        """
        :param ing: La fecha de recepción del lote con formato %d/%m/%Y
        :type ing: String
        :return: None
        """
        self.ingreso = ing

    def getFecha(self):
        """
        :return: La fecha de recepción del lote
        :rtype: DateTime
        """
        return self.ingreso

    def setMarca(self, marca):
        """
        :param marca: La marca de la vacuna
        :type marca: String
        :return: None
        """
        self.marca = marca

    def setNum(self, n):
        """
        :param n: El número de vacunas recibidas en el lote
        :type n: int
        :return: None
        """
        self.n = n

    def setRondas(self, r):
        """
        :param r: El número de aplicaciónes de la vacuna disponibles. Depende del tipo de vacuna, generalmente es 2.
        :type r: int
        :return: None
        """
        self.rondas = r

    def getMarca(self):
        """
        :return: La marca de la vacuna
        :rtype: String
        """
        return self.marca

    def getNum(self):
        """
        :return: El número de vacunas disponibles en el lote
        :rtype: int
        """
        return self.n

    def getRondas(self):
        """
        :return: El número de aplicaciones posibles, generalmente la mitad del total.
        :rtype: int
        """
        return self.rondas


def readLotes(fn, verbose=False, debug=False):
    """
    Lee la información de los lotes disponible en el archivo *fn* y la guarda en un objeto tipo :class:`~lotes.Lote`.

    :param fn: Ubicación del archivo con la información de lotes
    :type fn: String
    :param verbose: Opcional. Si es verdadero muestra información adicional al correrse.
    :type verbose: Boolean
    :param debug: Opcional. Si es verdadero muestra información útil para la depuración.
    :type debug: Boolean
    :return: Lista de Lotes con las variables leidas del archivo.
    :rtype: list
    """
    df = pd.read_csv(fn, encoding="latin")
    result = []
    i = 0
    for row in df.iterrows():
        i += 1
        if debug:
            print(row[1]['id_marca'])
        lote = Lote()
        lote.setId(row[1]['id_lote'])
        lote.setMarca(row[1]['id_marca'])
        lote.setIngreso(datetime.datetime.strptime(row[1]['fecha_ingreso'], "%d/%m/%Y"))
        lote.setNum(int(row[1]['num_vacunas']))
        result.append(lote)
    if verbose:
        print('Leidos ' + str(i) + ' lotes...')
    return result
