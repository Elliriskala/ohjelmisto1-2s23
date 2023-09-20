# def = define, funktion nimi (mahdolliset parametrit)

""""
def tervehdi():
    print("Moi!")
    print("Nyt ollaan funktion sisällä, ohjelman suoritus siirtyi tänne.")
    return # tällä palautetaan paluu arvo, mikäli semmoinen on

# pääohjelma
# jotat funktion rungossa olevaa koodia suoritettaisiin on funktiota kutsuttava
print("Terve, tämä on pääohjelma!")
# kutsutaan funktiota
tervehdi()
print("Jonka jälkeen tulimme pääohjelmaan.")

def tervehdi_käyttäjää():
    print("Moi taas!")
    return
def main():
    tervehdi_käyttäjää()

main()

"""
""""
# funktion parametrit
# kerrat = parametrimuuttuja
def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
# annetaan argumenttina arvo 5
tervehdi(5)
print("Tervehditään lisää.")
# argumenttina arvo 2
tervehdi(2)

# voidaan kysyä käyttäjältä
kertaa = int(input("Kuinka monta kertaa tervehditään? "))
tervehdi(kertaa)


# funktioiden parametrit ja paluuarvo
def print_summa(x, y):
    print(x + y)
    return

# funktiolle voi välittää useita argumentteja
# tämä funktio ei palauta mitään, joskus tämä on ihan OK
print_summa(5, 8)

def summa(x, y):
    yht = x + y
    return yht

tulos = summa(4, 77)
print(tulos)

# muita piirteitä
def tietoja(nimi, ikä, harrastus):
    tervehdys = f'Terve {nimi}. Ikäsi on {ikä} ja suosikkiharrastus: on {harrastus}.'
    return tervehdys

henkilö = tietoja("Elli", 21, "tennis")
print(henkilö)

# Parametrien välittäminen avainsanojen avulla.
# Ohjelmoija voi antaa parametrien arvot (nimi = arvo)-pareina.
# Parametreille voi antaa funktion määrityksessä myös oletusarvot.

henkilö2 = tietoja("Pekka", 23, harrastus = "tennis")
print(henkilö2)

# mitä jos en tiedä jotain argumenttia, miten voin kutsua funktiota?
def tietoja2(nimi, ikä, harrastus="ohjelmointi"):
    tervehdys = f'Terve {nimi}. Ikäsi on {ikä} ja suosikkiharrastus: on {harrastus}.'
    return tervehdys

henkilö3 = tietoja2("Pekka", 23)
print(henkilö3)



def print_city(city3):
    # lokaali muuttaja, arvo näkyy vain funktion sisällä (local scope)
    city = "Helsinki" # globaali muuttuja korvataan lokaalilla
    city2 = "Vantaa"
    print(city)
    print(city2)
    print(city3) # myö sfunktion parametrina esitelty muuttuja on lokaali
def print_city_v2():
    print(city) # tulostaa globaalin muuttujan arvon

# Globaali muuttuja arvo käytössä koko ohjelman laajuisesti (global scope)
# (jossei sitä "ylikirjoiteta" (shadows) jonkun funktion sisällä)
city = "Espoo"
print_city("Kirkkonummi")
print_city("Vihti")
print(city)
# print(city2) # city2 ei näy globaalisti, koska määritelty funktion sisällä
print_city_v2()


def list_reset(num):
    print("Nollataam kaikki listan alkiot: ")
    print(num)
    for i in range(5):
        num[i] = 0
    return num

numbers = [1, 2, 4, 7, 9]
print(list_reset(numbers))
print(numbers)

"""
def numbers_to_tuple(*nums):
    return nums

print(numbers_to_tuple(3, 6, 7, 2, 8))