name1 = "Ville"
name2 = "Viivi"
name3 = "Iines"
age1 = 5.5
age2 = 6
age3 = 38

# print(f"{name1}, ikä {age1} vuotta")

names = ["Ville", "Viivi", "Iines", "Ahmed", "Pekka", "Olga", "Mary"]
ages = [5.5, 6, 38, 5, 6, 23, 58]
# alkioon viitataan indeksinumerolla
# print(f"{names[0]}, ikä {ages[0]} vuotta")
# listan läpikäynti while-silmukalla

""""
i = 0
while i < len(names):
    print(f"{names[i]}, ikä {ages[i]} vuotta")
    i += 1
# eri tapoja viitata alkioihin
print(names[2:5]) # kolme alkiota alkaen indeksillä 2 edelleen lista-muodossa
print(names[-1]) # -1 viittaa aina viimeiseen
print(names[3:]) # kaikki loput alkiot alkaen alkaen indeksillä 3 lista-muodossa
# listan pituus len()
lenght = len(names)
print(lenght)
names.append("Uusi nimi") # uusi alkio listan loppuun
names.remove("Iines") # poistaa ekan Iines - arvon
names.insert(0, "Iines") # lisää uuden alkion haluttuun kohtaan (tässä alkuun indeksi 0)
print(names)
names.extend(ages) # ei virhettä, mutta yleensä huono käytäntö yhdistää erityyppisiä arvoja samalle listalle
print(names[8:])
ages2 = names[8:] # napataan tietty osa listasta uudeksi listaksi uuteen muuttujaan
print(ages2)
print(names.index(5.5))

# käyttäjän syötteen lisääminen listaan
newName = input("Anna uusi nimi: ")
names.append(newName)
# onko joku tietty arvo listalla?
searchTerm = input("Ketä etsit? ")
if searchTerm in names:
    print(f"Arvo {searchTerm} löytyy listalta")
else:
    print("ei löydy")
"""
print(names)
# listan alkioiden läpikäynti For-silmukalla
for name in names:
    print(f"Nimi: {name}")
# For-silmukka iteraattorilla = i
for i in range(7):  # 0, 1, 2, 3, 4, 5, 6
    print(f"Nimi {names[i]}")
for i in range(len(names)):  # 0, 1, 2, 3, -> name-listan pituus -1
    print(f"Nimi: {names[i]}, ikä: {ages[i]}")

# range esim.
for i in range(999, 0, -3):
    print(i)