kerrat = int(input("Montako kertaa tervehditään: "))
tehdyt = 0
while tehdyt < kerrat:
    print("Hyvää huomenta")
    tehdyt = tehdyt + 1

kerrat = int(input("Kuinka monta kertaa Musti haukkuu? "))
haukut = 0
while haukut < kerrat:
    print("Hau")
    haukut = haukut + 1

käsky = input("Musti haukkuu HAU HAU, niin pitkään kunnes sanot 'lopeta' ")

while käsky != 'lopeta':
    if käsky == "apua":
        break
    kerrat = 0
    while kerrat < 10:
        print("HAU")
        kerrat = kerrat + 1
    käsky = input("Musti haukkuu HAU HAU, niin pitkään kunnes sanot 'lopeta' ")
else:
    print("Annoit käskyn 'lopeta', ja musti lopetti haukkumisen.")

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka}")
        toka = toka + 1
    eka = eka + 1






