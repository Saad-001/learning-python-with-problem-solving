from tokenize import Number


def do_something(func, x , y) : 
    val= func(x, y)
    return val + 5

def pram_func(x, y) :
    return x + y

value = do_something(pram_func, 5, 5)
print(value)
