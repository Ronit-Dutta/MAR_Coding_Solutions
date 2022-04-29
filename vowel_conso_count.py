vo = co = 0
s = input("Enter the string")
s = s.lower()
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vo = vo + 1
    else:
        co = co + 1
print("Total number of vowels is : " + str(vo))
print("\n Total number of consonants is : " + str(co))