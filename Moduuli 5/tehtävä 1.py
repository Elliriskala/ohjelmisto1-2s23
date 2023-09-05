import random
heitot = int(input("Kuinka monta noppaa heitetään? "))
summa = 0
for i in range(heitot):
    i = random.randint(1,6)
    print(f"Heitetyt nopat: {i}")
    summa = summa + i
print(f"Heitettyjen noppien silmälukujen summa: {summa}")
