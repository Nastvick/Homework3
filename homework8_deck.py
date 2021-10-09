def my_deck(func, suits):
    for i in suits:
        yield func(i)

for i in my_deck(, range(4)):
    print(i)

