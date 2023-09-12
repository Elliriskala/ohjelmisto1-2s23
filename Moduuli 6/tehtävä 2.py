# tehtävä 1
# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
# satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

# tehtävä 2
# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä
# esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä
# poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
# nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

max_silmäluku = int(input("Kuinka monta tahkoa on nopassa jota heitetään? "))
def silmä_luku():
    print("Heitetään noppaa, kunnes saadaan syötetty tahko määrä.")
    luku = random.randint(1, max_silmäluku)
    print(f"Saatu silmäluku: {luku}")
    return luku

i = silmä_luku()
while i != max_silmäluku:
    i = silmä_luku()
else:
    print(f"Maksimi silmäluku, eli {max_silmäluku} saavuettu.")
