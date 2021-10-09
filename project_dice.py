import random

amount_of_dices = int(input("Choose amount of dices: "))

while True:
    target = int(input("Choose your target: "))
    if amount_of_dices <= target <= amount_of_dices * 6:
        break
    print("INCORRECT TARGET")

while True:
    dices = []
    for i in range(amount_of_dices):
        dices.append(random.randrange(1, 7))
    print("ROLLED DICES:", dices)
    if sum(dices) == target:
        print("YOU WON")
        break
    else:
        input("TRY AGAIN\n")









