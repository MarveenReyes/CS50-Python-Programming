while True:
    gas = input("How much gas?")

    splitted = gas.split('/')

    #Integer checker
    try:
        gas1 = splitted[0]
        gas2 = splitted[1]
    except:
        pass


    if gas1.isdigit() == False or gas2.isdigit() == False:
        continue
    else:
        pass



    try:
        numerator = int(gas1)
        denominator = int(gas2)
    except ValueError:
        pass

    if numerator > denominator:
        continue
    try:
        x = int(round((numerator/denominator)*100))
        break
    except ZeroDivisionError:
        pass
    else:
        pass
if x >= 99:
    print("F")
elif x <= 1:
    print("E")
else:
    print(str(x) + "%")
