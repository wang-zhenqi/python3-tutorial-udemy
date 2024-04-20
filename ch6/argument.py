# Variable number of arguments *args
def add(*args):
    print(args)
    result = 0
    for i in args:
        result += i
    return result

print(add(1, 2, 3, 4))

# Variable number of arguments **kwargs
def mult(**kwargs):
    print(kwargs)
    result = 1
    for i in kwargs.values():
        result *= i
    return result

print(mult(a = 1, b = 2, c = 3))

# Default value of arguments
def default_value(a, b = 10):
    return a + b

print(default_value(5))
print(default_value(5, 20))