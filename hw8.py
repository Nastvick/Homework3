import itertools

c = itertools.chain([1, 2, 3], [4, 5, 6], [7, '888', 9])

for i in range(9):
    print(next(c))