'''Escribir un programa que solicite al usuario una vocal en minuscula,y luego una letra
en mayúscula. El programa debe convertir la letra en minúscula y la vocal en mayúscula, 
y al final, deben ser concatenadas ambas'''

minus=input('Introduce vocal minuscula: ')
mayus=input('Introduce letra mayuscula: ')

resultado = mayus.lower() + minus.upper()
print('Letra en minuscula y vocal en mayuscula concatenadas: ' + resultado)