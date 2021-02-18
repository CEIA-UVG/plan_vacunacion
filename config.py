"""
=========
config.py
=========

Clase encargada de leer y mantener los datos de configuración del programa. Consta de una clase llamada
:class:`~config.ConfigParams` que guarda todos los valores obtenidos del archivo ``config.txt``, y el método
:func:`~config.readConfig` que lee el archivo ``config.txt`` y obtiene los valores que se granab en ConfigParams.
Esta clase es utilizada por el programa principal :mod:main.py únicamente al inicio para cargar los valores de
``config.txt``. """


class ConfigParams:
    """
    Guarda los valores leidos de ``config.txt``
    """
    def __init__(self, numestacionespordependencia, numvacunasporestacionpordia,
                 tiempoparallevarvacunasaestacion, pesoedad, pesohabita,
                 pesotrabaja, pesocargo, pesocovid, pesodiabetes, pesopeso,
                 pesocancer, pesovih, pesorenal):
        """
        :param numestacionespordependencia: Número de estaciones de vacunación por centro de adscripción.
        :type numestacionespordependencia: integer
        :param numvacunasporestacionpordia: Número máximo de vacunas diarias que cada estación puede administrar.
        :type numvacunasporestacionpordia: integer
        :param tiempoparallevarvacunasaestacion: Número de días que toma llevar las vacunas hasta cada centro.
        :type tiempoparallevarvacunasaestacion: integer
        :param pesoedad: Peso que se le asigna a la prioridad de la edad. Debe ser >= 0, recomendado igual a 1.
        :type pesoedad: integer
        :param pesohabita: Peso que se le asigna a la prioridad del municipio donde el paciente reside. Debe ser >= 0.
        :type pesohabita: integer
        :param pesotrabaja: Peso que se le asigna a la prioridad del lugar de trabajo. Debe ser >= 0, recomendado = 1.
        :type pesotrabaja: integer
        :param pesocargo: Peso que se le asigna a la prioridad del cargo que desempeña. Debe ser >= 0, recomendado = 1.
        :type pesocargo: integer
        :param pesocovid: Peso que se le asigna a la prioridad de haber tenido previamente COVID19. Debe ser >= 0.
        :type pesocovid: integer
        :param pesodiabetes: Peso que se le asigna a la prioridad de tener diabetes miellitus. Debe ser >= 0.
        :type pesodiabetes: integer
        :param pesopeso: Peso que se le asigna a la prioridad de tener sobrepeso. Debe ser >= 0, recomendado igual a 1.
        :type pesopeso: integer
        :param pesocancer: Peso que se le asigna a la prioridad de haber tenido o tener cancer. Debe ser >= 0.
        :type pesocancer: integer
        :param pesovih: Peso que se le asigna a la prioridad de ser VIH positivo. Debe ser >= 0, recomendado igual a 1.
        :type pesovih: integer
        :param pesorenal: Peso que se le asigna a la prioridad de tener alguna enfermedad renal. Debe ser >= 0.
        :type pesorenal: integer
        """
        self.numEstacionesPorDependencia = numestacionespordependencia
        self.numVacunasPorEstacionPorDia = numvacunasporestacionpordia
        self.tiempoParaLlevarVacunasAEstacion = tiempoparallevarvacunasaestacion
        self.pesoEdad = pesoedad
        self.pesoHabita = pesohabita
        self.pesoTrabaja = pesotrabaja
        self.pesoCargo = pesocargo
        self.pesoCovid = pesocovid
        self.pesoDiabetes = pesodiabetes
        self.pesoPeso = pesopeso
        self.pesoCancer = pesocancer
        self.pesoVih = pesovih
        self.pesoRenal = pesorenal

    def getNumEstacionesPorDepencencia(self):
        """
        :return: número de estaciones de vacunación por centro de adscripción
        :rtype: integer
        """
        return self.numEstacionesPorDependencia

    def getNumVacunasPorEstacionPorDia(self):
        """
        :return: número máximo de vacunas que cada centro puede administrar en un día.
        :rtype: integer
        """
        return self.numVacunasPorEstacionPorDia

    def getTiempoParaLlevarVacunasAEstacion(self):
        """
        :return: días requeridos para llevar las vacunas a los centros de adscripción.
        :rtype: integer
        """
        return self.tiempoParaLlevarVacunasAEstacion

    def getPesoEdad(self):
        """
        :return: peso de la prioridad por edad
        :rtype: int
        """
        return self.pesoEdad

    def getPesoHabita(self):
        """
        :return: peso de la prioridad por municipio donde reside.
        :rtype: int
        """
        return self.pesoHabita

    def getPesoTrabaja(self):
        """
        :return: peso de la prioridad por lugar donde trabaja
        :rtype: int
        """
        return self.pesoHabita

    def getPesoCargo(self):
        """
        :return: peso de la prioridad por cargo que ocupa
        :rtype: int
        """
        return self.pesoCargo

    def getPesoCovid(self):
        """
        :return: peso de la prioridad por haber tenido COVID19 previamente
        :rtype: int
        """
        return self.pesoCovid

    def getPesoDiabetes(self):
        """
        :return: peso de la prioridad por tener diabetes miellitus
        :rtype: int
        """
        return self.pesoDiabetes

    def getPesoPeso(self):
        """
        :return: peso de la prioridad por tener sobrepeso
        :rtype: int
        """
        return self.pesoPeso

    def getPesoCancer(self):
        """
        :return: peso de la prioridad por tener o haber tenido cancer
        :rtype: int
        """
        return self.pesoCancer

    def getPesoVih(self):
        """
        :return: peso de la prioridad por ser VIH positivo
        :rtype: int
        """
        return self.pesoVih

    def getPesoRenal(self):
        """
        :return: peso de la prioridad por tener alguna enfermedad renal
        :rtype: int
        """
        return self.pesoRenal


def readConfig(fn):
    """
    Lee las variables de configuración del archivo especificado.

    :param fn: Ubicación del archivo ``config.txt``
    :type fn: String
    :return: Objeto ConfigParams con las variables leidas del archivo.
    :rtype: ConfigParams
    """
    f = open(fn)
    lines = f.readlines()
    f.close()

    numestacionespordependencia = int(lines[0].split(' ')[0])
    numvacunasporestacionpordia = int(lines[1].split(' ')[0])
    tiempoparallevarvacunasaestacion = int(lines[2].split(' ')[0])
    pesoedad = int(lines[3].split(' ')[0])
    pesohabita = int(lines[4].split(' ')[0])
    pesotrabaja = int(lines[5].split(' ')[0])
    pesocargo = int(lines[6].split(' ')[0])
    pesocovid = int(lines[7].split(' ')[0])
    pesodiabetes = int(lines[8].split(' ')[0])
    pesopeso = int(lines[9].split(' ')[0])
    pesocancer = int(lines[10].split(' ')[0])
    pesovih = int(lines[11].split(' ')[0])
    pesorenal = int(lines[12].split(' ')[0])

    result = ConfigParams(numestacionespordependencia, numvacunasporestacionpordia,
                          tiempoparallevarvacunasaestacion, pesoedad, pesohabita,
                          pesotrabaja, pesocargo, pesocovid, pesodiabetes, pesopeso,
                          pesocancer, pesovih, pesorenal)
    return result
