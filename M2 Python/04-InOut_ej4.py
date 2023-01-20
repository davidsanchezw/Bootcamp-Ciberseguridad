'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha 
obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, 
el examen parcial y el examen final. Considere:
PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final'''

p1 = float(input("Introduce nota de P1: "))
p2 = float(input("Introduce nota de P2: "))
p3 = float(input("Introduce nota de P3: "))
ep = float(input("Introduce nota de EP: "))
ef = float(input("Introduce nota de EF: "))

pp = ( p1 + p2 +p3 ) / 3
prom = ( pp + 2*ep + 3*ef ) / 6

print("La nota promedio de practica es: {}".format(round(pp,2)))
print("La nota promedio es: {}".format(round(prom, 2)))

