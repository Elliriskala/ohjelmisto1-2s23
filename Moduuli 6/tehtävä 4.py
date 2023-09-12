# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def list_sum(nums):
    print("Lasketaan alla olevan listan alkioiden summa: ")
    print(nums)
    result = 0
    for num in nums:
        result = result + num
    return result

numbers = [1, 2, 4, 7, 9]
print(list_sum(numbers))
numbers_sum = list_sum([2, 4, -10])
print(numbers_sum)



