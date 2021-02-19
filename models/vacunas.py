"""
==========
vacunas.py
==========

Clase encargada de leer y mantener los datos acerca de las vacunas. Consta de una clase llamada
:class:`~vacunas.Vacuna` que guarda todos los valores relevantes a las vacunas, y el método
:func:`~vacunas.readVacunas` que lee los datos del archivo con la información de las vacunas y los graba en una
instancia de la clase Vacuna.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores acerca
de las vacunas.
"""
import pandas as pd


class Vacuna:
    """
    Guarda la información de una vacuna: id, marca, número de dosis, tiempo entre dosis, temperatura de almacenamiento y
    observaciones.
    """
    def __init__(self):
        self.id = ""
        self.marca = ""
        self.dosis = -1
        self.tiempo = -1
        self.temp = ""
        self.obs = ""

    def __str__(self):
        return self.marca + "\t" + str(self.dosis) + "\t" + str(self.tiempo)

    def setId(self, i):
        """
        :param i: El código de identificación único de cada vacuna
        :type i: String
        :return: None
        """
        self.id = i

    def setMarca(self, marca):
        """
        :param marca: La marca de la vacuna
        :type marca: String
        :return: None
        """
        self.marca = marca

    def setDosis(self, dosis):
        """
        :param dosis: El número de dosis requerido por la vacuna
        :type dosis: int
        :return: None
        """
        self.dosis = dosis

    def setTiempo(self, tiempo):
        """
        :param tiempo: El número de semanas entre las dosis de la vacuna
        :type tiempo: int
        :return: None
        """
        self.tiempo = tiempo

    def getTiempo(self):
        """
        :return: El número de semanas entre las dosis de la vacuna
        :rtype: int
        """
        return self.tiempo

    def setTemp(self, temp):
        """
        :param temp: La temperatura a la que se debe almacenar la vacuna
        :type temp: Stirng
        :return: None
        """
        self.temp = temp

    def setObs(self, obs):
        """
        :param obs: Cualquier otra información u observación relevante de la vacuna
        :type obs: String
        :return: None
        """
        self.obs = obs

    def getId(self):
        """
        :return: El código de identificación de la vacuna
        :rtype: String
        """
        return self.id

    def getDosis(self):
        """
        :return: El número de dosis de la vacuna
        :rtype: int
        """
        return self.dosis


def readVacunas(fn, verbose=False, debug=False):
    """
    Lee la información de las vacunas disponible en el archivo *fn* y la guarda en un objeto
    tipo :class:`~vacunas.Vacuna`.

    :param fn: Ubicación del archivo con la información de las vacunas.
    :type fn: String
    :param verbose: Opcional. Si es verdadero muestra información adicional al correrse.
    :type verbose: Boolean
    :param debug: Opcional. Si es verdadero muestra información útil para la depuración.
    :type debug: Boolean
    :return: Lista de Vacunas con las variables leidas del archivo.
    :rtype: list
    """
    df = pd.read_csv(fn, encoding="latin")
    result = {}
    i = 0
    for row in df.iterrows():
        i += 1
        if debug:
            print(row[1]['marca'])
        v = Vacuna()
        v.setId(row[1]['id_marca'])
        v.setMarca(row[1]['marca'])
        v.setDosis(int(row[1]['dosis']))
        if row[1]['tiempo_dosis (semanas)'] != "":
            v.setTiempo(float(row[1]['tiempo_dosis (semanas)']))
        else:
            v.setTiempo(-1.0)
        v.setTemp(row[1]['temp_conserv'])
        v.setObs(row[1]['observaciones'])
        result[v.getId()] = v
    if verbose:
        print('Leidas ' + str(i) + ' tipos de vacunas...')
    return result
