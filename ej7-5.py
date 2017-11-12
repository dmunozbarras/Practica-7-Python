# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 7 - EJERCICIO 5
Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una
función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada.
Devolverá la función la frase modificada, y el programa principal la imprimirá:
"""
def cambia(x,vocal):
    for i in x:
        if i =='a' or i =='e' or i =='i' or i =='o' or i =='u' or i =='A' or i =='E' or i =='I' or i =='O' or i =='U':
            x= x.replace(i, vocal)
    return x

texto=raw_input("Dime algo: ")
vocal2=raw_input("Dime una vocal para cambiar en todo el texto: ")

a=cambia(texto, vocal2)

print (a)
