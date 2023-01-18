'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver 
el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá 
aplicar un 21%.'''

def func():
    val = float(input("Introduce valor: "))
    iva = input("Introduce IVA: ")
    
    if len(iva) == 0:
        iva = 21
    else:
        iva = float(iva)
        
    res = val + val * iva / 100
    print ("El valor es: {}".format(res))
        
        
func()