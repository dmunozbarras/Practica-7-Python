# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 7 - EJERCICIO 4
Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. La
función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el
resultado para que el programa principal la imprima por pantalla.
"""

def cambia(x):
    cambia= texto.replace(' ', '*')
    return cambia


texto=raw_input("Escriba un texto: ")

a=cambia(texto)

print (a)
