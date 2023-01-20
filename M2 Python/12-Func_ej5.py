'''Escribir una función que reciba una muestra de números en una lista y devuelva su medida.'''

def func(elemento):
    print (type(elemento))
    for i in elemento:
        print(i)           
    return len(elemento)

lista = [1, 2, 3, 4, 5]
print("Elementos en [1,2,3,4,5] = {}".format(func(lista)))