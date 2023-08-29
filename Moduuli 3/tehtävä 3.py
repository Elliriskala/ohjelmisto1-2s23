sukupuoli = input("Mikä on biologinen sukupuolesi? ")
if sukupuoli == "nainen":
    hg_arvo_n = float(input("Mikä on hemoglobiiniarvosi g/l? "))
    if 117 <= hg_arvo_n <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    if hg_arvo_n < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    if hg_arvo_n > 175:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "mies":
    hg_arvo_m = float(input("Mikä on hemoglobiiniarvosi g/l? "))
    if 134 <= hg_arvo_m <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    if hg_arvo_m < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    if hg_arvo_m > 195:
        print("Hemoglobiiniarvosi on korkea.")





