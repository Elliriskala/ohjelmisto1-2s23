# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä
# kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math
def pyöreä_pitsa(halkaisija, hinta):
    return hinta/(math.pi * (halkaisija/2)**2)

halkaisija = float(input("Mikä on ensimmäisen pitsan halkaisija senttimetreinä? "))
hinta = float(input("Montako euroa ensimmäinen pitsa maksaa? "))
halkaisija2 = float(input("Mikä on toisen pitsan halkaisija senttimetreinä? "))
hinta2 = float(input("Montako euroa toinen pitsa maksaa? "))

# print("Pitsa maksaa", pyöreä_pitsa(halkaisija, hinta), "euroa per neliömetri.")
# print("Pitsa maksaa", pyöreä_pitsa(halkaisija2, hinta2), "euroa per neliömetri.")

pitsa1 = pyöreä_pitsa(halkaisija, hinta)
pitsa2 = pyöreä_pitsa(halkaisija2, hinta2)

if pitsa1 > pitsa2:
    print("Jälkimmäinen pitsa on halvempi vaihtoehto.")
elif pitsa1 < pitsa2:
    print("Ensimmäinen pitsa on halvempi vaihtoehto.")
else:
    print("Pitsat ovat samanhintaisia.")
