dict={'1' : "Casillas", '15' : "Ramos", '3' : "Pique", '5' : "Puyol", '11' : "Capdevila", '14' : "Xabi Alonso",
'16' : "Busquets", '8' : "Xavi Hernandez", '18' : "Pedrito", '6' : "Iniesta", '7' : "Villa"}

num = input("Introduce un numero: ").title()

if num in dict:
    print ("El numero {} es de {}".format(num, dict.get(num)))
else:
    print("No se encuentra el jugador")