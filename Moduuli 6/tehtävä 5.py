# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten
# samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

import random
def even_numbers(list):
    output = []
    for i in list:
        if i % 2 == 0:
            output.append(i)
    return output

my_list = []
for i in range(20):
    i = random.randint(1,100)
    my_list.append(i)

print(even_numbers(my_list))
print(my_list)


