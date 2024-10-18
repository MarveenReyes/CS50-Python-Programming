dicts = {}
while True:
    try:
        ing = input().upper()
        if ing not in dicts:
            dicts[ing] = 1
        else:
            dicts[ing] += 1
    except EOFError:
        break

sorted_dict = dict(sorted(dicts.items()))
for item in sorted_dict:
    print(sorted_dict[item],item)

