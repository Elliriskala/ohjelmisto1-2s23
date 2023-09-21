# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa
# lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Elli',
    password='koira12',
    autocommit=True
)


def get_distance_between_airports(ICAO):
    cursor = connection.cursor()
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{ICAO}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result


def calculate_distance(airport1, airport2):
    return geodesic(airport1, airport2).km


ICAO1 = input("Syötä valitsemasi lentokentän ICAO-koodi: ").upper()
ICAO2 = input("Syötä toisen valitsemasi lentokentän ICAO-koodi: ").upper()

airport1 = get_distance_between_airports(ICAO1)
airport2 = get_distance_between_airports(ICAO2)

if airport1 is None or airport2 is None:
    print("Syöttämääsi ICAO-koodia ei löytynyt.")
else:
    distance = calculate_distance(airport1, airport2)
    print(f"Välimatka valitsemiesi lentokenttien {ICAO1} ja {ICAO2} välillä on: {distance:.2f} kilometriä.")
