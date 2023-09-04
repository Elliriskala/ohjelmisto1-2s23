smallest = 0
largest = 0
user_input = input("Syötä luku tai 'Enter' lopettaaksesi: ")
n = user_input

if user_input != '':
    n = float(user_input)
    smallest = n
    largest = n
while user_input != '':
    user_input = input("Syötä luku tai 'Enter' lopettaaksesi: ")
    if user_input == '':
        break
    n = float(user_input)
    if n <= smallest:
        smallest = n
    elif n >= largest:
        largest = n

print("Syötit 'enter' ja lukujen syöttäminen päättyi. ")
print(f"Pienin syöttämäsi luku: {smallest}")
print(f"Suurin syöttämäsi luku: {largest}")
