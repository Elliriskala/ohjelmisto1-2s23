vuosi = int(input("Ilmoita vuosiluku: "))
if vuosi %400 == 0:
    print("Vuosi on karkausvuosi.")
elif vuosi %400 == 0 or vuosi %4 == 0 and vuosi %100 != 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi")

