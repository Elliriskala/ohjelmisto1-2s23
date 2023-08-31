#Kirjoitetaan ohjelma joka tulostaa tulostaa tuumia senttimetreiksi:
tuuma = 1
while tuuma >= 0:
    tuuma = float(input("Montako tuumaa muutetaan senttimetreiksi? "))
    if tuuma < 0:
        print("Ohjelma lopetti toimintansa")
        quit()
    print(f"{tuuma * 2.54} cm")

