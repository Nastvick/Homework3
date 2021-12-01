def deco_adds_2(f):
    def inner(**args, **kwargs):
        res = f(a, b)+2
        print('AFTER WITH RESULT', res)
        return res
    return inner

@deco_adds_2
def add_sum(a, b):
     return a + b


print(add_sum(10, 10))  # >>> 22
print(add_sum(2, 3))  # >>> 7