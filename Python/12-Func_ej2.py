def factorial1(num):
    res = 1
    while num:
        res *= num
        num -= 1
    return res

def factorial2(num):
    if num == 1:
        return 1
    return num * factorial2(num - 1)
       
num = int(input("Introduce valor a factorizar: "))
if num > 0:
    print("El resultado es {}".format(factorial1(num)))
    print("El resultado en funcion recursiva es {}".format(factorial2(num)))
else:
    print("Valor no aceptado")