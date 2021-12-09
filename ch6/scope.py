# different scope in and out of function
x = 1
x += 1
print(x)

def demo():
    x = 10
    a = 11
    a = a + x
    print(a)
    print(x)

demo()
print(x)

# passing value to function
def demo(a):
    a = a + 10
    print(a)

demo(a = x)
print(x)

# passing reference to function
y = [1, 2, 3]
print(y)

def demo1(a):
    a.append(4)
    print(a)

demo1(a = y)
print(y)

# global
z = 1
print(z)

def demo2(a):
    global z
    z = z + a
    print(z)

demo2(a = 10)
print(z)
