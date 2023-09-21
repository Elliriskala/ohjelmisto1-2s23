# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee
# ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
# lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Elli',
    password='koira12',
    autocommit=True
    )

def get_airports_by_ICAO(ICAO):
    cursor = connection.cursor()
    sql = f"select municipality, name from airport where ident = '{ICAO}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result


airport = get_airports_by_ICAO(input("Mikä on etsimäsi lentokentän ICAO-koodi: "))

if airport is None:
    print("Syöttämääsi ICAO-koodia ei löytynyt.")
else:
    print(f"Tulostetaan syöttämääsi ICAO-koodia vastaava lentokenttä ja sijaintikunta. "
          f"Lentokenttä: {airport[1]}, sijaintikunta: {airport[0]}")




