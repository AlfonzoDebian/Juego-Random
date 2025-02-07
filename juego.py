

import random
print("Juego.py")
print("Escoje una opcion: ")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
print("No vale <1 o >3")

tu = int(input("Con que vaz a jugar (?): "))
cp =  random.randrange(1, 3)

############## empate
if cp == tu:
    print("========================================")
    print("Empate")
    print("========================================")
elif tu <1 or tu >3:
    print("========================================")
    print("Valor no VALIDO. ")
    print("=======================================")
elif (tu == 1 and cp == 2 ) or (tu == 2 and cp == 3 ):
    print("========================================")
    print("GAME OVER")
    print("=======================================")
elif (tu == 2 and cp == 1 ) or (tu == 3 and cp == 2 ):
    print("========================================")
    print("Winner. ")
    print("=======================================")



print("CP ESCOJIO", cp)