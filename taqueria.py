menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


total = 0
while True:

    try:
        order = input("Item: ").title()
        x = menu.get(order)
        total = total + x
        print(f'Total: ${total:.2f}')
    except KeyError:
        pass
    except TypeError:
        pass
    except EOFError:
        break





