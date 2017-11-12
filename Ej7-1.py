# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 7 - EJERCICIO 1
Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un
procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.
"""

def cambio(x):
    print x.lower()
    print x.upper()

texto=raw_input("Escriba un texto: ")
cambio(texto)
