def my_chain(*col):
    for i in col:
        for c in i:
            yield c


col = my_chain([1, 2, 3], [4, 5, 6], [7, '888', 9])

for c in col:
    print(c)

