# Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan
# litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän
# ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen
# gallonamäärän.Yksi gallona on 3,785 litraa.

def bensiinin_määrä(gallonat):
    litrat = 3.785 * gallona
    return litrat

gallona = 1
while gallona > 0:
    gallona = float(input("Kuinka monta gallonaa syötetään litroiksi? "))
    if gallona < 0:
        break
    else:
        print(f"{bensiinin_määrä(gallona)} l")
