# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan
# vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = {1: 'talvi', 2: 'talvi', 3: 'kevät', 4: 'kevät', 5: 'kevät', 6: 'kesä', 7: 'kesä', 8: 'kesä', 9: 'syksy', 10: 'syksy', 11: 'syksy', 12: 'talvi'}
kuukausi = int(input("Syötä haluamasi kuukauden järjestysluku (1-12): "))
vuodenaika = vuodenajat[kuukausi]
print(f"{kuukausi}. kuukausi on vuodenaikana: {vuodenaika}")