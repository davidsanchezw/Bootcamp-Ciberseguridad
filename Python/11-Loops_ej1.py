'''Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar 
de ese numero'''

num = int(input("Introduce un numero: "))

i = 0
while 10 >= i:
    print ("{} x {} = {}".format(num, i, num*i))
    i += 1