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
        self.tiempo = 1
        self.n1a = -1
        self.n1b = -1
        self.n1c = -1
        self.n2a = -1
        self.n2b = -1
        self.n2c = -1
        self.n2d = -1
        self.n3a = -1
        self.n4a = -1
        self.n4b = -1
        self.n4c = -1
        self.n4d = -1

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

    def setTiempo(self,tiempo):
        """
        :param tiempo: Tiempo en dias requerido para llevar las vacunas a la clinica
        :type: int
        :return: None
        """
        self.tiempo = tiempo

    def getTiempo(self):
        """
        :return: Tiempo en dias requerido para llevar las vacunas a la clinica.
        :rtype: int
        """
        return self.tiempo

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

    def setN1b(self, n1b):
        """
        :param n1b: Cantidad de personas de la fase 1b que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n1b = n1b

    def getN1b(self):
        """
        :return: Número de personas de la fase 1b que esta clínica debe atender.
        :rtype: int
        """
        return self.n1b

    def setN1c(self, n1c):
        """
        :param n1c: Cantidad de personas de la fase 1c que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n1c = n1c

    def getN1c(self):
        """
        :return: Número de personas de la fase 1c que esta clínica debe atender.
        :rtype: int
        """
        return self.n1c

    def setN2a(self, n2a):
        """
        :param n2a: Cantidad de personas de la fase 2a que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n2a = n2a

    def getN2a(self):
        """
        :return: Número de personas de la fase 2a que esta clínica debe atender.
        :rtype: int
        """
        return self.n2a

    def setN2b(self, n2b):
        """
        :param n2b: Cantidad de personas de la fase 2b que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n2b = n2b

    def getN2b(self):
        """
        :return: Número de personas de la fase 2b que esta clínica debe atender.
        :rtype: int
        """
        return self.n2b

    def setN2c(self, n2c):
        """
        :param n2c: Cantidad de personas de la fase 2c que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n2c = n2c

    def getN2c(self):
        """
        :return: Número de personas de la fase 2c que esta clínica debe atender.
        :rtype: int
        """
        return self.n2c

    def setN2d(self, n2d):
        """
        :param n2d: Cantidad de personas de la fase 2d que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n2d = n2d

    def getN2d(self):
        """
        :return: Número de personas de la fase 2d que esta clínica debe atender.
        :rtype: int
        """
        return self.n2d

    def setN3a(self, n3a):
        """
        :param n3a: Cantidad de personas de la fase 3a que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n3a = n3a

    def getN3a(self):
        """
        :return: Número de personas de la fase 3a que esta clínica debe atender.
        :rtype: int
        """
        return self.n3a

    def setN4a(self, n4a):
        """
        :param n4a: Cantidad de personas de la fase 4a que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n4a = n4a

    def getN4a(self):
        """
        :return: Número de personas de la fase 4a que esta clínica debe atender.
        :rtype: int
        """
        return self.n4a

    def setN4b(self, n4b):
        """
        :param n4b: Cantidad de personas de la fase 4b que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n4b = n4b

    def getN4b(self):
        """
        :return: Número de personas de la fase 4b que esta clínica debe atender.
        :rtype: int
        """
        return self.n4b

    def setN4c(self, n4c):
        """
        :param n4c: Cantidad de personas de la fase 4c que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n4c = n4c

    def getN4c(self):
        """
        :return: Número de personas de la fase 4c que esta clínica debe atender.
        :rtype: int
        """
        return self.n4c

    def setN4d(self, n4d):
        """
        :param n4d: Cantidad de personas de la fase 4d que esta clínica debe atender.
        :type: int
        :return: None
        """
        self.n4d = n4d

    def getN4d(self):
        """
        :return: Número de personas de la fase 4d que esta clínica debe atender.
        :rtype: int
        """
        return self.n4d

    def getMaxPerPhase(self,fase):
        """
        Recibe el nombre de la fase y devuelve el numero de vacunas a aplicar en dicha fase.
        :param fase: Nombre de la fase de vacunacion
        :type fase: String
        :return: Numero de vacunas a aplicar en *fase*
        :rtype: int
        """
        if fase == 'n1a':
            return self.n1a
        elif fase == 'n1b':
            return self.n1b
        elif fase == 'n1c':
            return self.n1c
        elif fase == 'n2a':
            return self.n2a
        elif fase == 'n2b':
            return self.n2b
        elif fase == 'n2c':
            return self.n2c
        elif fase == 'n2d':
            return self.n2d
        elif fase == 'n3a':
            return self.n3a
        elif fase == 'n4a':
            return self.n4a
        elif fase == 'n4b':
            return self.n4b
        elif fase == 'n4c':
            return self.n4c
        elif fase == 'n4d':
            return self.n4d
        else:
            print("ERROR: " + fase + " no es una fase valida!")
            return -1

    def __str__(self):
        return self.name + "\t" + self.departamento + "\t" + self.municipio + "\t" + str(self.capacidad) + "\t" + \
               str(self.tiempo) + "\t" + str(self.n1a) + "\t" + str(self.n1b) + "\t" + str(self.n1c) + "\t" + \
               str(self.n2a) + "\t" + str(self.n2b) + "\t" + str(self.n2c) + "\t" + str(self.n2d) + "\t" + \
               str(self.n3a) + "\t" + str(self.n4a) + "\t" + str(self.n4b) + "\t" + str(self.n4c) + "\t" + \
               str(self.n4d)


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
            print(row)
        c = Clinica()
        c.setCapacidad(int(row[1]['vaccCap']))
        c.setName(row[1]['dependencia'])
        c.setTiempo(row[1]['tiempo'])

        lat = float(row[1]['latitud'])
        lon = float(row[1]['longitud'])
        c.setCodigo(row[1]['codigo'])
        c.setDepartamento(row[1]['departamento'])
        c.setMunicipio(row[1]['municipio'])
        c.setLat(lat)
        c.setLon(lon)
        if row[1]['n1a'] != 'NaN':
            c.setN1a(int(row[1]['n1a']))
        if row[1]['n1b'] != 'NaN':
            c.setN1b(int(row[1]['n1b']))
        if row[1]['n1c'] != 'NaN':
            c.setN1c(int(row[1]['n1c']))
        if row[1]['n2a'] != 'NaN':
            c.setN2a(int(row[1]['n2a']))
        if row[1]['n2b'] != 'NaN':
            c.setN2b(int(row[1]['n2b']))
        if row[1]['n2c'] != 'NaN':
            c.setN2c(int(row[1]['n2c']))
        if row[1]['n2d'] != 'NaN':
            c.setN2d(int(row[1]['n2d']))
        if row[1]['n3a'] != 'NaN':
            c.setN3a(int(row[1]['n3a']))
        if row[1]['n4a'] != 'NaN':
            c.setN4a(int(row[1]['n4a']))
        if row[1]['n4b'] != 'NaN':
            c.setN4b(int(row[1]['n4b']))
        if row[1]['n4c'] != 'NaN':
            c.setN4c(int(row[1]['n4c']))
        if row[1]['n4d'] != 'NaN':
            c.setN4d(int(row[1]['n4d']))

        result.append(c)
    if verbose:
        print('Leidas ' + str(i) + ' dependencias...')
    return result
