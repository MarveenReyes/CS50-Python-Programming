def snake(word):
    word = list(word)
    for i,letter in enumerate(word):
        if letter.isupper():
            word[i] = "_"+letter.lower()
    return "".join(word)


camel = input("camelCase: ")
print("snake_case:", snake(camel))

