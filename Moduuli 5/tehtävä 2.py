nums = []
user_input = input("Syötä luku tai paina 'enter' lopettaksesi ohjelman: ")
if user_input != '':
    num = float(user_input)
    nums.append(num)
while user_input != '':
    user_input = input("Syötä luku tai paina 'enter' lopettaksesi ohjelman: ")
    if user_input == '':
        break
    num = float(user_input)
    nums.append(num)

print("Painoit 'enter' ja ohjelma lopetti toimintansa")

if user_input == "x":
    print("Väärä merkki, ohjelma lopetti toimintansa")
else:
    nums.sort(reverse=True)
    print(f"Suurimmat viisi syötettyä lukua: ", nums[:5])






