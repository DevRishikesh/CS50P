text=str(input("Input: "))
vowels="aeiouAEIOU"
newtext=""
for c in text:
    if c not in vowels:
        newtext += c

print(newtext)
