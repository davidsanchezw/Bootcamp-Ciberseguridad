'''Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de
la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>'''

user=input('Introduce tu usuario: ')
age=int(input('Introduce edad: '))
gender=input('Introduce sexo: ')

print('Te llamas: {}\nTu edad es: {}\nEres:{}'.format(user, age, gender))