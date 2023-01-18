'''Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario 
un número, el que haya ingresado, es la letra que debe imprimir el programa'''

letra= ("a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","x","y","z")

numletra = int(input("Introduce numero de la letra: "))

print("{}".format(letra[numletra - 1]))