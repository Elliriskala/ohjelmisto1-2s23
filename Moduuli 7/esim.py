# monikko eli tuple, "kuin lista jota ei voi muokata"
""""
def numbers_to_tuple(*nums):
    for num in nums:
        print(num)
    return nums

print(numbers_to_tuple(3, 6, 7, 2, 8))

numbers = (4, 7, 9, 4)
print(numbers)

numbers = (8, 5, 9, 6)
print(numbers)

minun_lista = [1,2,3,4,5,6]
print(minun_lista)

minun_monikko = (1,2,3,4,5,6)
print(minun_monikko)
minun_monikko2 = 1,2,3,4,5,6
print(minun_monikko2)

minun_string = "123456"

# muokataan niitä
# listan sisältöä voi muokata, mutable
minun_lista[0] = 0
print(minun_lista)

# monikon ja string EI voi muokata, imutable
# minun_monikko[0] = 0
# minun_string[0] = 0

viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
# jos käyttäjä syöttää arvon 1
# viikonpäivä = viikonpäivät[3]
# print(päivä)

järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))

viikonpäivä = viikonpäivät[järjestysnumero-1]
print(f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

# monikko voidaan purkaa muuttujiin

hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")
"""
# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat
# olla missä tahansa järjestyksessä. Koska joukon alkioille ei ole
# määritelty järjestystä, ei alkioihin voi myöskään viitata indeksillä.

minun_monikko = (1,2,3,4,5,6)
minun_monikko = (1,56,3,4,5,6)
print(minun_monikko)

minun_lista = [1,2,3,4,5,6]
minun_lista = [1,2,3,44,5,6]
print(minun_lista)
minun_set = {"Monopoli", "Shakki", "Cluedo"}
print(minun_set)

minun_set.add("Dominion")
print(minun_set)

# Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa
# vain kertaalleen, eli joukossa ei voi olla kahta samansisältöistä alkiota.

minun_lista2 = [1,2,3,4,5,1]
print(minun_lista2)

minun_set2 = {1,2,3,4,5,1}
print(minun_set2)

for i in minun_set2:
    print(i)

# sanakirja

oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 16, 'Daniel': 45, 'Emma': 34}

# printataan koko sanakirja
for i in oppilaat:
    print(i)

# arvot
for i in oppilaat:
    print(oppilaat[i])

# mitä ovat tietueet/items
print(oppilaat.items())

# mitkä ovat avaimia sanakirjassa
print(oppilaat.keys())

# mitkä ovat arvoja sanakirjassa
print(oppilaat.values())

oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 16, 'Daniel': 45, 'Emma': 34}

print(oppilaat["Daniel"])

# lisätään, mikäli ei löydy
oppilaat['Fredrik'] = 67

for i in oppilaat:
    print(i)

oppilaat['Aapeli'] = 26
print(oppilaat.items())

nimi = input("Anna nimi: ")
if nimi in oppilaat:
    print(f"Henkilön {nimi} ikä on {oppilaat[nimi]}.")

# poista tietue
del oppilaat['Daniel']
print(oppilaat.items())

# toinen tapa poistaa, tallenna Aapelin tiedot muuttujaan

aapelin_ikä = oppilaat.pop('Aapeli')
print(f"Aapeli poistettiin, mutta ikä jäi talteen: {aapelin_ikä}")
print(oppilaat.items())

# luodaan uusi oppilas, jolla aapelin tiedot
oppilaat['Pekka'] = aapelin_ikä
print(oppilaat.items())
