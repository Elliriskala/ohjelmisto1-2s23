# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Elli',
    password='koira12',
    autocommit=True
    )

