# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
# haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon
# miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

airports = {'EFHK': 'Helsinki-Vantaa', 'LIPZ': 'Venice Marco Polo Airport', 'ESSA': 'Stockholm-Arlanda Airport', 'EKCH': 'Copenhagen Airport', 'EGKK': 'London-Gatwick Airport'}

while True:
    user_input = input("Haluatko syöttää uuden lentoaseman 'uusi'vai hakea jo syötetyn lentoaseman tiedot 'vanha' vai lopettaa painamalla 'enter'? ")
    if user_input == 'uusi':
        airport_ICAO = input("Syötä uuden lentoaseman ICAO-koodi? ")
        airport_ICAO = airport_ICAO.upper()
        airport_name = input("Mikä on lentokentän nimi? ")
        airport_name = airport_name.casefold().capitalize()
        airports[airport_ICAO] = airport_name
    elif user_input == 'vanha':
        airport_ICAO = input("Mikä on lentoaseman ICAO-koodi? ")
        airport_ICAO = airport_ICAO.upper()
        if airport_ICAO in airports:
            airport_name = airports[airport_ICAO]
            print(f"Syötetty ICAO koodi {airport_ICAO} on {airport_name}")
    elif user_input == '':
        break

print("Ohjelman suoritus lopetettu.")