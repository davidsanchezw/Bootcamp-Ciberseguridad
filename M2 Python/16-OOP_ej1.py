'''Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos 
el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def setNombre(self, nombre):
        self.nombre = nombre
        
    def setNota(self, nota):
        self.nota = nota

    def printAtributos(self):
        print("Nombre: {}".format(self.nombre))
        print("Nota: {}".format(self.nota))
        
    def isAprobado(self):
        if self.nota >= 5:
            print("Aprobado")
        else:
            print("Suspenso")
            
estudiante = Estudiante("Pepe", 2)
estudiante.printAtributos()
estudiante.isAprobado()