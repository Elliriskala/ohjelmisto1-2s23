import random
arvaukset = 0
arvaus = input
numero = random.randint(1,10)
while (arvaus != numero):
    arvaus = int(input("Arvaa kokonaisluku 1-10 väliltä: "))
    arvaukset = arvaukset + 1
    if arvaus > numero:
        print("Liian suuri arvaus.")
    if arvaus < numero:
        print("Liian pieni arvaus.")
else:
    if arvaus == numero:
        print("Oikein.")

