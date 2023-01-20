'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, 
el que haya ingresado, es el mes que debe mostrar en la tupla'''

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

nummes = int(input("Introduce numero del mes: "))

print("{}".format(meses[nummes - 1]))