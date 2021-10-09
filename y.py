def my_filter(func, col):
    for i in col:
     if func(i):
         yield i

g = my_filter(lambda x: x % 2 == 0, range(10))
for i in g:
    print(i)

def my_map(func, col):
    for i in col:
        yield func(i)

for i in my_map(lambda x:x ** 2, range(10)):
    print(i)

