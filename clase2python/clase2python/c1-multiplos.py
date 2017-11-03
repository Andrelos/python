#!/usr/bin/env python
# -*- coding: utf-8 -*-

def multiplos(maximo):
    """
    Retorna una lista con números que simultáneamente son múltiplos
    de 3 y 5, hasta un valor máximo especificado.
    """
    # Lista a retornar.
    ret = []
    # Recorrer una lista con todos los números desde el 1 hasta
    # el máximo indicado.
    for numero in range(1, maximo+1):
        # Chequear que la división por 3 y 5 del número actual
        # sea exacta.
        if numero % 3 == 0 and numero % 5 == 0:
            ret.append(numero)
    return ret


print multiplos(10000)
