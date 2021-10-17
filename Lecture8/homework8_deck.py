def my_deck(*suits):
    for i in suits:
        yield i

def my_deck(*values):
    for i in values:
        yield i

for i in my_deck("Hearts", "Diamonds", "Clubs", "Spades"):
    print(i)

for i in my_deck('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
    print(i)






