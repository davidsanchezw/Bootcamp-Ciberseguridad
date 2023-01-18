'''Escribe un programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco
y si no, que no riman.'''

var1 = input("Introduce la primera palabra: ")
var2 = input("Introduce la segunda palabra: ")
if len(var1) < 2 and len(var2) < 2:
    if var1[-3:] == var2[-3:]:
        print("Riman")
    elif var1[-2:] == var2[-2:]:
        print("Riman un chin")
else:
    print("No riman")