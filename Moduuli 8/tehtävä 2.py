# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Elli',
    password='koira12',
    autocommit=True
    )

def get_airport_type_by_iso_country(iso_country, airport_type):
    sql = f"select type from airport where airport.iso_country = '{iso_country}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount <= 0:
        print("No results. ")
        return -1
    for row in result:
        if row[0] in airport_type:
            airport_type[row[0]] += 1
    print(f"Syöttämälläsi maakoodilla: '{iso_country}' saadut lentokentät: '{airport_type}'")
    return


airport_type = {'heliport': 0,
                'small_airport': 0,
                'medium_airport': 0,
                'large_airport': 0,
                'closed': 0
}

iso_country = input("Ohjelma tulostaa maakoodilla kyseisen maan lentokentät. Syötä haluamasi maakoodi: ").upper()
get_airport_type_by_iso_country(iso_country, airport_type)





