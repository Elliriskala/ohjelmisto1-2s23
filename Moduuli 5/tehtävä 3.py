# jos luku on alle kaksi, niin koodia on turha suorittaa
user_input = int(input("Syötä kokonaisluku joka on suurempi kuin numero 2: "))
number = user_input
isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        # print("Numero ei ole alkuluku. ")

print("Alkuluku testi suoritettu: ")
if isPrime:
    print(f"Luku {number} on alkuluku")
else:
    print(f"Luku {number} ei ole alkuluku")

