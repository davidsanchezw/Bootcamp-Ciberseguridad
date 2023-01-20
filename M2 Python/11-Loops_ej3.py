'''Imprimir por pantalla los numeros del 1 al 10, luego pedir al usuario dos numeros y 
mostrar el rango de numeros entre ambas cifras'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    print(i)

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: ".format(num1)))
if num2 > num1:
    for i in range(num1, num2 + 1,1):
        print(i)
else:
    for i in range(num2, num1 + 1,1):
        print(i)