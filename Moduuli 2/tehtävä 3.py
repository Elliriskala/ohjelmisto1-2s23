num1 = int(input("Mikä on suorakulmion kanta? "))
num2 = int(input("Mikä on suorakulmion korkeus? "))
# lasketaan suorakulmion piiri = k + k + k + k
# lasketaan suorakolmion pinta-ala = kanta*korkeus

print(f"Suorakulmion piiri: {(num1 + num1 + num2 + num2)}")
print(f"Suorakulmion pinta-ala: {(num1 * num2)}")
