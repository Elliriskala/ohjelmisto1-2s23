tunnus = "python"
salasana = "rules"
kerrat = 0

while kerrat < 5:
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")
    if tunnus != "python" or salasana != "rules":
        print("Pääsy evätty")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        quit()
    kerrat = kerrat + 1
print("Käyttäjätunnus ja salasana syötetty 5 kertaa väärin.")

