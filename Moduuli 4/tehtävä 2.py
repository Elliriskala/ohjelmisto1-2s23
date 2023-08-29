#Kirjoitetaan ohjelma joka tulostaa tulostaa tuumia senttimetreiksi:

tuuma = float(input("Montako tuumaa muutetaan senttimetreiksi? "))
print(f"{tuuma * 2.54} cm")
while tuuma >= 0:
    tuuma = float(input("Montako tuumaa muutetaan senttimetreiksi? "))
    print(f"{tuuma * 2.54} cm")
    if tuuma < 0:
        print("Ohjelma lopetti toimintansa")

