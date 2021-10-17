def my_fizz_buzz(n):
    if x % 3 == 0 and x % 5 == 0:
        return 'fizz buzz'
    elif x % 3 == 0:
        return 'fizz'
    elif  x % 5 == 0:
        return 'buzz'
    else:
        return x
n = 16
for x in range(1,n+1):
    print (my_fizz_buzz(x))