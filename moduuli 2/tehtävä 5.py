# yksi leiviskä = 20 naulaa
# yksi naula = 32 luotia
# yksi luoti = 13.3g

luoti = 13.3
naula = 32 * luoti
leiviskä = 20 * naula

# print(f"{32 * luoti}")
# print(f"{20 * naula}")

num1 = float(input("Anna leiviskät: "))
num2 = float(input("Anna naulat: "))
num3 = float(input("Anna luodit: "))

result = num1 * leiviskä + num2 * naula + num3 * luoti
kg = int(result // 1000)
g = result % 1000

print(f"Kokonaismassa nykymittojen mukaan: {(num1 * leiviskä + num2 * naula + num3 * luoti)/1000}")
print(f"Massa nykymittojen mukaan kg: {kg}")
print(f"Massa nykymittojen mukaan g: {g:.3f}")
