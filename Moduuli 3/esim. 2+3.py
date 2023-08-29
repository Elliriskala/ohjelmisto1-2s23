suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari == räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")

#ehtorakenne

user_input = input("a vai b? ")

if user_input == "a":
    print("Tee jotain.")
    print("ja jatka sitä")
elif user_input == "b":
    print("käyttäjä valitsi b:een")
    print("tehdään jotain muuta")
else:
    print("käyttäjä ei syöttänyt a:ta eikä b:tä, ei tehdä mitään.")

print("ohjelman suoritus jatkuu tästä.")

# Loogiset operaattorit
# and = molemmat, or = toinen, not = kääntää sueraavan boolean arvon käänteiseksi
age = 5
name = "Ville"
print(age < 10)
print(name == "Ville")
print(age < 10 and name == "Ville")

age = int(input("Anna age: "))
if 15 <= age < 18:  # sama ehto toisin: (15 <= age) and (age < 18)
    paino = float(input("Anna paino (kg): "))
    if paino >= 55:
        print("Lääkkeen käyttö on sallittua.")
elif age >= 18:
    print("Lääkkeen käyttö on sallittua.")




