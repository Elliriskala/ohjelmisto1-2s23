# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
# satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def silmä_luku():
    print("Heitetään noppaa, kunnes saadaan silmäluvuksi 6.")
    luku = random.randint(1,6)
    print(f"Saatu silmäluku: {luku}")
    return luku

i = silmä_luku()
while i != 6:
    i = silmä_luku()
else:
    print("Sait silmäluvuksi: 6")




