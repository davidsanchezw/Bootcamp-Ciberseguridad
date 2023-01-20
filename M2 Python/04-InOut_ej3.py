'''Realizar un programa que haga el proceso de formula general para la resolución de 
ecuaciones, sabiendo que la formula general es la que está en la imagen 
(-b + sqrt(b*b - 4 * a * c)) / (2 * a), el usuario 
debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso 
para que al final muestre el mensaje: “La solución es: <solucion>'''

# importar libreria
from math import sqrt

# bucle para inputs y comprobar positivismo dentro de la raiz
while True:
    a = int(input('Introduce a: '))
    b = int(input('Introduce b: '))
    c = int(input('Introduce c: '))
    
    if 0 <= b**b - 4 * a * c:
        break 
print ('Inputs correctos')

# Realizar operación
resultado1 = (-b + sqrt(b*b - 4 * a * c)) / (2 * a)
resultado2 = (-b - sqrt(b*b - 4 * a * c)) / (2 * a)
if resultado1 == resultado2:
    print ("resultado: {}".format(resultado1))
else:
        print ("resultado 1: {}\nresultado 2: {}".format(resultado1, resultado2))
