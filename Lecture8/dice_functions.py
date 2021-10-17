def dices(amount_of_dices):
    while True:
        target = int(input("Choose your target: "))
        if amount_of_dices <= target <= amount_of_dices * 6:
            break
        return "INCORRECT TARGET"

    while True:
        dices = []
        for i in range(amount_of_dices):
            dices.append(random.randrange(1, 7))
        return ("ROLLED DICES:", dices)
        if sum(dices) == target:
            return "YOU WON"
            break
        else:
            input("TRY AGAIN\n")

