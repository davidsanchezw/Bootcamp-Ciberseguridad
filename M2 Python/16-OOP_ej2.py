"""Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el 
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un 
método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora."""

class Calculadora:
    def __init__(self):
        self.int1 = int(input("Introduce un numero: "))
        self.int2 = int(input("Introduce otro numero: "))
        
    def sum(self):
        return self.int1 + self.int2
    
    def res(self):
        return self.int1 - self.int2
    
    def mul(self):
        return self.int1 * self.int2
    
    def div(self):
        return self.int1 / self.int2
    
calculadora = Calculadora()
print(calculadora.sum())
print(calculadora.res())
print(calculadora.mul())
print(calculadora.div())