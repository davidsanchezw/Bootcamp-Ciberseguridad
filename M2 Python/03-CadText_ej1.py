'''Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo” 
Ej.: Si la cadena fuera “recta” debería imprimir rca
• Dicha cadena en sentido inverso. 
Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. 
Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

frase = "Te quiero solo como amigo"

print(frase[::2])
print (frase + frase[::-1])