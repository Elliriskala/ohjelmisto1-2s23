countries = []
for i in range(5):
    country = input("Syötä haluamasi kaupunki: ")
    countries.append(country)

print("Syötetyt viisi kaupunkia: ")
for country in range(5):
    print(f"{countries[country]}")
