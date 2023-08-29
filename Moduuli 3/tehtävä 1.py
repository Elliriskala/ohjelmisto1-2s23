kuhan_pituus = float(input("Ilmoita kuhan pituus senttimetreinä? "))
if kuhan_pituus >= 37:
    print("Kuha on sopivan mittainen")
elif kuhan_pituus < 37:
    print("Kuha on alamittainen, laske se takaisin järveen.")
    print(f"Alimmasta pyyntimitasta puuttuu:{37 - kuhan_pituus: 0.1f} cm.")


