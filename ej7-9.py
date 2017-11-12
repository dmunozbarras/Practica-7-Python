# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 7 - EJERCICIO 9
Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si
riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman.
"""

def rimar (palabra3,palabra4,palabra5,palabra6):
    if palabra3==palabra4:
        print "riman"
    elif palabra5==palabra6:
        print "riman poco"
    else:
        print "no riman"

pal1=raw_input("Escriba la palabra 1: ")
pal2=raw_input("Escriba la palabra 1: ")
pal3= pal1[-3:]
pal4= pal2[-3:]
pal5= pal1[-2:]
pal6= pal2[-2:]

rimar(pal3,pal4,pal5,pal6)


"""
pal1=raw_input("Escriba la palabra 1: ")
pal2=raw_input("Escriba la palabra 1: ")
pal3= pal1[-3:]
pal4= pal2[-3:]
pal5= pal1[-2:]
pal6= pal2[-2:]

if pal3==pal4:
    print "riman"
elif pal5==pal6:
    print "riman poco"
else:
    print "no riman"
"""
