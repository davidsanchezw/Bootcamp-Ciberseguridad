'''Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado 
con argumentos de base y altura; y la otra el area de un circulo con argumento de radio'''

from math import pi

def cuadrado(lado):
    return lado * lado
def circulo(radio):
    return pi * radio * radio

print("Area del cuadrado: {}".format(cuadrado(5)))
print("Area del circulo: {}".format(circulo(7)))