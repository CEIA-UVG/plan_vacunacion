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
    def __init__(self, numestacionespordependencia, numvacunasporestacionpordia, tiempoparallevarvacunasaestacion,
                 pesoedad, pesohabita, pesotrabaja, pesocargo, pesocovid, pesodiabetes, pesopeso, pesocancer, pesovih,
                 pesorenal, path_to_files, archivo_pacientes, archivo_lotes, archivo_cargos, archivo_edad, archivo_muni,
                 archivo_unidades, archivo_vacunas, archivo_clinicas, archivo_excluidos, archivo_vacunados):
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
        :param path_to_files: Folder relativo donde se encuentran los archivos de entrada.
        :type path_to_files: String
        :param archivo_pacientes: Nombre del archivo con datos de los pacientes
        :type archivo_pacientes: String
        :param archivo_lotes: Nombre del archivo con datos de los lotes
        :type archivo_lotes: String
        :param archivo_cargos: Nombre del archivo con datos de los cargos
        :type archivo_cargos: String
        :param archivo_edad: Nombre del archivo con datos de las edades
        :type archivo_edad: String
        :param archivo_muni: Nombre del archivo con datos de los municipios donde habitan los pacientes
        :type archivo_muni: String
        :param archivo_unidades: Nombre del archivo con datos de las unidades de vacunacion
        :type archivo_unidades: String
        :param archivo_vacunas: Nombre del archivo con datos de las vacunas
        :type archivo_vacunas: String
        :param archivo_clinicas: Nombre del archivo con datos de las clinicas
        :type archivo_clinicas: String
        :param archivo_excluidos: Nombre del archivo con datos de los pacientes a excluir
        :type archivo_excluidos: String
        :param archivo_vacunados: Nombre del archivo con datos de los pacientes vacunados
        :type archivo_vacunados: String
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
        self.path_to_files = path_to_files
        self.archivo_pacientes = archivo_pacientes
        self.archivo_clinicas = archivo_clinicas
        self.archivo_edad = archivo_edad
        self.archivo_muni = archivo_muni
        self.archivo_unidades = archivo_unidades
        self.archivo_vacunas = archivo_vacunas
        self.archivo_lotes = archivo_lotes
        self.archivo_cargos = archivo_cargos
        self.archivo_excluidos = archivo_excluidos
        self.archivo_vacunados = archivo_vacunados

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

    def getPathToFiles(self):
        """
        :return: path relativo a los archivos de entrada
        :rtype: String
        """
        return self.path_to_files

    def getFileLotes(self):
        """
        :return: nombre del archivo de lotes
        :rtype: String
        """
        return self.archivo_lotes

    def getFileVacunas(self):
        """
        :return: nombre del archivo de vacunas
        :rtype: String
        """
        return self.archivo_vacunas

    def getFileUnidades(self):
        """
        :return: nombre del archivo de unidades
        :rtype: String
        """
        return self.archivo_unidades

    def getFileMuni(self):
        """
        :return: nombre del archivo de municipios
        :rtype: String
        """
        return self.archivo_muni

    def getFileEdad(self):
        """
        :return: nombre del archivo de edad
        :rtype: String
        """
        return self.archivo_edad

    def getFileClinicas(self):
        """
        :return: nombre del archivo de clinicas
        :rtype: String
        """
        return self.archivo_clinicas

    def getFilePacientes(self):
        """
        :return: nombre del archivo de pacientes
        :rtype: String
        """
        return self.archivo_pacientes

    def getFileCargos(self):
        """
        :return: nombre del archivo de cargos
        :rtype: String
        """
        return self.archivo_cargos

    def getFileExcluidos(self):
        """
        :return: nombre del archivo de exlcuidos
        :rtype: String
        """
        return self.archivo_excluidos

    def getFileVacunados(self):
        """
        :return: nombre del archivo de vacunados
        :rtype: String
        """
        return self.archivo_vacunados


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
    path_to_files = lines[13].split(' ')[0]
    archivo_pacientes = lines[14].split(' ')[0]
    archivo_lotes = lines[15].split(' ')[0]
    archivo_cargos = lines[16].split(' ')[0]
    archivo_edad = lines[17].split(' ')[0]
    archivo_muni = lines[18].split(' ')[0]
    archivo_unidades = lines[19].split(' ')[0]
    archivo_vacunas = lines[20].split(' ')[0]
    archivo_clinicas = lines[21].split(' ')[0]
    archivo_excluidos = lines[22].split(' ')[0]
    archivo_vacunados = lines[23].split(' ')[0]

    result = ConfigParams(numestacionespordependencia, numvacunasporestacionpordia, tiempoparallevarvacunasaestacion,
                          pesoedad, pesohabita, pesotrabaja, pesocargo, pesocovid, pesodiabetes, pesopeso, pesocancer,
                          pesovih, pesorenal, path_to_files, archivo_pacientes, archivo_lotes, archivo_cargos,
                          archivo_edad, archivo_muni, archivo_unidades, archivo_vacunas, archivo_clinicas,
                          archivo_excluidos, archivo_vacunados)
    return result
