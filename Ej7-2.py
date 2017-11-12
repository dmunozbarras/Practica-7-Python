# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 7 - EJERCICIO 2
Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de
caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver
una única cadena. La cadena final la imprimirá el programa por pantalla.
"""
def unir(x,y,z):
    nombre=x+' '+y+' '+z

    return nombre

nom=raw_input("Escriba el nombre: ")
apell1=raw_input("Escriba el primer apellido: ")
apell2=raw_input("Escriba el segundo apellido: ")
a=unir(nom, apell1, apell2)
print (a)
