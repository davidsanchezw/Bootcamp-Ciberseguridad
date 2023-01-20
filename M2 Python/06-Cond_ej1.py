'''Crear un programa que pida al usuario una letra, y si es vocal, 
muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal'''

x = input("Introduce una letra: ")

if (x == "a"or x == "e"or x == "i"or x == "o"or x == "u"):
    print("{} es vocal".format(x))
elif x.isalpha():
    print("{} es consonante".format(x))
else:
    print("{} no es una letra".format(x))