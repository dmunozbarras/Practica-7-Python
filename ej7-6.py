# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 7 - EJERCICIO 6
Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una
función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo
imprimirá el programa principal por pantalla.
"""


def buscar(nom,cara):
    num= 0
    for i in range (0,len(nom)):
        if nom[i] == (cara):
            num= num+ 1
    return num





nom2 = str(raw_input("Introduce un nombre: "))
cara2= str(raw_input("Introduce un caracter: "))


num2=buscar(nom2,cara2)
print "%s esta en el nombre %s %d veces" % (cara2, nom2, num2)





""" Sin funcion
nom = str(raw_input("Introduce un nombre: "))
cara= str(raw_input("Introduce un caracter: "))
num= 0
for i in range(0, len(nom)):
    if nom[i] == (cara):
        num = num + 1
print "%s esta en el nombre %s %d veces" % (cara, nom, num)
"""
