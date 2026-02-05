# Voici notre premier project
# nous voulons un code python qui permet a l'utilisateur de deviner un nombre:
# Entrer un nombre, et quand l'utilisateur entre le nombre, ça dit si le nombre entré est grand ou petit. ou il a trouver le bon nombre
import random
nombre_devine=random.randint(1,20)

print("=============Bienvenue dans le jeu de devinette !===========")
print("Je pense à un nombre entre 1 et 20. Pouvez-vous deviner lequel ?")
for tentative in range(1, 10):
    devine=int(input("Entrez votre devinette : "))
    if devine < nombre_devine:
        print("Trop bas ! Essayez encore.")
    elif devine > nombre_devine:
        print("Trop haut ! Essayez encore.")
    else:
        print(f"Félicitations ! Vous avez deviné le nombre {nombre_devine} en {tentative} tentatives.")
        break
