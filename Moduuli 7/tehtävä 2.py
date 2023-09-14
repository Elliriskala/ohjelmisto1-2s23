# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == '':
        break
    elif nimi not in nimet:
        print("Uusi nimi.")
    elif nimi in nimet:
        print("Aiemmin syötetty nimi.")
    nimet.add(nimi)

print("Painoit 'enter' ja ohjelma lopetti toimintansa")
print("Tulostetaan syötetyt nimet mielivaltaisessa järjestyksessä: ")

for i in nimet:
    print(i)

