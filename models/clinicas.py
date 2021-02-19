"""
===========
clinicas.py
===========

Clase encargada de leer y mantener los datos acerca de las clínicas / centros de vacunación. Consta de una clase llamada
:class:`~clinicas.Clinica` que guarda todos los valores relevantes a las clínicas, y el método
:func:`~clinicas.readClinicas` que lee los datos del archivo con la información de las clínicas y los graba en una
instancia de la clase Clinica.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores acerca
de las clinicas.

"""
import pandas as pd


class Clinica:
    """
    Guarda la información de una clínica:
    * Nombre de la clínica.
    * Código de la clínica.
    * Departamento donde se encuentra la clínica.
    * Municipio donde se encuentra la clínica.
    * Latitud y Longitud donde se encuentra la clínica.
    * Capacidad de atención de la clínica.
    * Las cantidades de personas por fase y subfase que esta clínica debe atender.
    """
    def __init__(self):
        self.name = ""
        self.codigo = -1
        self.departamento = ""
        self.municipio = ""
        self.lat = -1
        self.lon = -1
        self.capacidad = -1
        self.n1a = -1
        self.n1b = -1
        self.n1c = -1
        self.n2a = -1
        self.n2b = -1
        self.n2c = -1
        self.n2d = -1
        self.n2e = -1
        self.n3a = -1
        self.n4a = -1
        self.n4b = -1
        self.n4c = -1
        self.n4d = -1
        self.n4e = -1

    def setName(self, name):
        """
        :param name: Nombre de la clínica
        :type: String
        :return: None
        """
        self.name = name

    def getName(self):
        """
        :return: Nombre de la clínica
        :rtype: String
        """
        return self.name

    def setCapacidad(self, capacidad):
        """
        :param capacidad: Capacidad de la atención de la clínica
        :type: int
        :return: None
        """
        self.capacidad = capacidad

    def getCapacidad(self):
        """
        :return: Capacidad de atención de la clínica
        :rtype: int
        """
        return self.capacidad

    def setCodigo(self, codigo):
        """
        :param codigo: Código de la clínica
        :type: String
        :return: None
        """
        self.codigo = codigo

    def getCodigo(self):
        """
        :return: Nombre de la clínica
        :rtype: String
        """
        return self.codigo

    def setDepartamento(self, departamento):
        """
        :param departamento: Departamento donde se ubica la clínica
        :type: String
        :return: None
        """
        self.departamento = departamento

    def setMunicipio(self, municipio):
        """
        :param municipio: Municipio donde se ubica la clínica
        :type: String
        :return: None
        """
        self.municipio = municipio

    def setLat(self, lat):
        """
        :param lat: Latitud donde se ubica la clínica
        :type: float
        :return: None
        """
        self.lat = lat

    def setLon(self, lon):
        """
        :param lon: Longitud donde se ubica la clínica
        :type: float
        :return: None
        """
        self.lon = lon

    def setN1a(self, n1a):
        """
        :param n1a: Cantidad de personas de la fase 1a que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n1a = n1a

    def getN1a(self):
        """
        :return: Número de personas de la fase 1a que esta clínica debe atender.
        :rtype: int
        """
        return self.n1a

    def __str__(self):
        return self.name + "\t" + self.departamento + "\t" + self.municipio + "\t" + \
               str(self.capacidad) + "\t" + \
               str(self.n1a)


def readClinicas(fn, verbose=False, debug=False):
    """
    Lee la información de las clínicas disponible en el archivo *fn* y la guarda en un objeto
    tipo :class:`~clinicas.Clinica`.

    :param fn: Ubicación del archivo con la información de las clinicas.
    :type fn: String
    :param verbose: Opcional. Si es verdadero muestra información adicional al correrse.
    :type verbose: Boolean
    :param debug: Opcional. Si es verdadero muestra información útil para la depuración.
    :type debug: Boolean
    :return: Lista de Clinicas con las variables leidas del archivo.
    :rtype: list
    """
    df = pd.read_csv(fn, encoding="latin")
    result = []
    i = 0
    for row in df.iterrows():
        i += 1
        if debug:
            print(row[1]['vaccCap'], row[1]['dependencia'])
        c = Clinica()
        c.setCapacidad(int(row[1]['vaccCap']))
        c.setName(row[1]['dependencia'])

        lat = float(row[1]['latitud'])
        lon = float(row[1]['longitud'])
        c.setCodigo(row[1]['codigo'])
        c.setDepartamento(row[1]['departamento'])
        c.setMunicipio(row[1]['municipio'])
        c.setLat(lat)
        c.setLon(lon)
        c.setN1a(int(row[1]['n1a']))
        result.append(c)
    if verbose:
        print('Leidas ' + str(i) + ' dependencias...')
    return result
