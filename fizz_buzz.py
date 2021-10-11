def my_fizz_buzz(n):
    for x in range(1,n+1):
        if x % 3 == 0 and x % 5 == 0:
            yield 'fizz buzz'
        elif x % 3 == 0:
            yield 'fizz'
        elif  x % 5 == 0:
            yield 'buzz'
        else:
            yield x

for x in my_fizz_buzz(16):
    print(x)