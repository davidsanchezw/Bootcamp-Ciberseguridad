'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos 
los años que ha cumplido (desde 1 hasta su edad).'''

num = int(input("Introduce tu edad: "))

i = 1
print ("Has cumplido: ")
edades = []
while num >= i:
    edades.append(i)
    i += 1
print ("{} años".format(edades))