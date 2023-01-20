'''Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, 
pero, solo imprimiendo los números que sean impares'''

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: ".format(num1)))
if num2 > num1:    
    for i in range(num1, num2 + 1, 1):
        if  not i % 2:
            continue
        print(i)
else:
    if not num2 % 2:
        num2 += 1
    for i in range(num2, num1 + 1, 1):
        if  not i % 2:
            continue
        print(i)