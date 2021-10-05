import random

#amount_of_dices =
sum_of_dices = random.randint(2, 12)
sum_of_dices = random.randint(3, 18)

while True:
    amount_of_dices = int(input("Choose amount of dices: "))
    if amount_of_dices == 2:
        sum_of_dices == random.randint(2, 12)
    if amount_of_dices == 3:
        sum_of_dices = random.randint(3, 18)
    target = int(input("Choose your target: "))
    if target == sum_of_dices:
        print(f"Roll is {sum_of_dices}")
        print("You are win!")
        break
    elif target > sum_of_dices:
        print(f"Roll is {sum_of_dices}")
        print("You did not guess! Try again")
        break
    else:
        print(f"Roll is {sum_of_dices}")
        print("You did not guess! Try again")
        break









