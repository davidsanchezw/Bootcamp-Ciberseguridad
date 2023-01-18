'''En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes 
realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado 
caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no 
se encuentra.'''
dict={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
      "Nicaragua": "Managua", "Costa Rica": "San Jose","Panama": "Panama", 
      "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", 
      "España": "Madrid"}

pais = input("Introduce pais: ").title()


if dict.get(pais):
    print ("La capital de {} es {}".format(pais, dict.get(pais)))
else:
    print("No se encuentra el pais")