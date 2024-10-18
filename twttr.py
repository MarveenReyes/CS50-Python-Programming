vowels = ["a","e","i","o","u",]
word = list(input("Input: "))
shortword = []
for letter in word:
    if letter.lower() not in vowels:
        shortword.append(letter)
print("".join(shortword))
