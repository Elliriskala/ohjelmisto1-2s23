import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Elli',
    password='koira12',
    autocommit=True
    )

"""
cursor = connection.cursor()
# cursor.execute("select iso_country, name from country where iso_country = 'FI'")
cursor.execute("select iso_country, name, continent from country")
result = cursor.fetchall() # cursor.fetchone = hakee vain ensimmäisen tulosrivin
print(result) # koko tulosjoukko listana
print(cursor.rowcount) # tulosrivien määrä
cursor.execute("select iso_country, name, continent from country")
# for i in range(0, 248):
    # result2 = cursor.fetchone()
    # print(result2)

for country in result: # country: yksi tulosjoukon rivi monikkona
    print(f"Maa: {country[1]}, koodi: {country[0]}")

"""
# ICAO = ident
def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    cursor.execute(f"select iso_country, name from country where iso_country = '{iso_code}'")
    result = cursor.fetchone()
    if result:
        return result[1]
    else:
        return "No results."

country = get_country_by_iso_code('FI')
print(country)
country = get_country_by_iso_code(input("Hae maakoodilla: "))
print(country)

def update_country_by_iso_code(iso_code, country_name):
    cursor = connection.cursor()
    sql = (f"update country set name='{country_name}' where iso_country='{iso_code}'")
    cursor.execute(sql)
    if cursor.rowcount > 0:
        return f"Koodi {iso_code} päivitetty, uusi maan nimi: {country_name}"
    else:
        return f"Koodia {iso_code} ei löytynyt. Muutoksia ei tehty."

country_code = input("Anna muokattava koodi: ")
new_name = input("Anna maalle uusi nimi: ")
update_result = update_country_by_iso_code(country_code, new_name)
print(update_result)