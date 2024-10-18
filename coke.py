amountdue = 50

while amountdue > 0:
    print("Amount Due:",amountdue)
    payment = int(input("Insert Coin: "))
    if payment == 5 or payment == 10 or payment == 25:
        amountdue -= payment
if amountdue < 0:
    amountdue = abs(amountdue)

print("Change Owed:",amountdue)
