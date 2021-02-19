"""
===============
asignaciones.py
===============

Clase encargada de leer y mantener los datos acerca de las asignaciones de vacunas. Consta de una clase llamada
:class:`~asignaciones.Asignacion` que guarda todos los valores relevantes a las asignaciones.
Esta clase es utilizada por el programa principal :mod:main.py al final para devolver los valores acerca
de las asignaciones que es el resultado final.
"""


class Asignacion:
    """
    Guarda la información de una asignación:
    * Código de identificación de la asignación.
    * Código de la vacuna.
    * Número de dosis.
    * Unidad de vacunación donde se utilizará esta vacunación.
    * Orden de prioridad para vacunación.
    * Fecha de vacunación de la asignación.
    """
    def __init__(self, i, vacuna, dosis, dependencia, orden, fecha):
        self.id = i
        self.vacuna = vacuna
        self.dosis = dosis
        self.dependencia = dependencia
        self.orden = orden
        self.fecha = fecha

    def __str__(self):
        return self.id + "," + str(self.dependencia) + "," + \
               str(self.vacuna) + "," + str(self.dosis) + "," + str(self.orden) + "," + \
               str(self.fecha)
