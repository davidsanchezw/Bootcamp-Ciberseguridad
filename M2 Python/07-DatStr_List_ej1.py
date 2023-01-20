'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario,
a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos 
en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]'''

list = [20, 50, "Curso", 'Python', 3.14]

list[0] = input("LISTA INICIAL\n\t{}\nIntroduce valor a sustituir en la lista en la primer posición: ".format(list))
list[1] = input("\t{}\nIntroduce valor a sustituir en la lista en la segunda posición: ".format(list))
print("Valor de la lista final\n\t{}".format(list))