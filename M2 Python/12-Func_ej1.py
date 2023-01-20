'''Crear un programa que tenga una lista, luego crear una funcion con la cual se van a 
pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en 
donde se ordenen los numeros pares e impares dentro de dos listas nuevas'''

list = []
listpar = []            
listimpar = []

def appendlist():
    for i in range(1, 7):
        num = int(input("Introduce valor a añadir a la lista: "))
        list.append(num)
    
def sortlist():
    list.sort()
    for i in list:
        if  i % 2:
            listpar.append(i)
        else:
            listimpar.append(i)
            
appendlist()
sortlist()
print("Lista ordenada de numeros pares: {}".format(listpar))
print("Lista ordenada de numeros impares: {}".format(listimpar))