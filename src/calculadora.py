import math


class NoSePuedeCalcular(Exception):
    pass


def calcular_media(elementos):
    if len(elementos) == 0:
        raise NoSePuedeCalcular("La lista está vacía")

    if not all(isinstance(i, (int, float)) for i in elementos):
        raise TypeError("Todos los elementos deben ser números")

    return sum(elementos) / len(elementos)


def calcular_desviacion_estandar(elementos):
    if len(elementos) == 0:
        raise NoSePuedeCalcular("La lista está vacía")

    if not all(isinstance(i, (int, float)) for i in elementos):
        raise TypeError("Todos los elementos deben ser números")

    media = calcular_media(elementos)
    varianza = sum((x - media) ** 2 for x in elementos) / len(elementos)

    return math.sqrt(varianza)
