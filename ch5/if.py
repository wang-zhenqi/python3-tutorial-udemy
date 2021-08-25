# if statement
if 1 > 0:
    print("1 > 0")
    print(1 < 0)

a = int(input("enter a number: "))
print(a, type(a))

if a > 0:
    print('This is a number larger than zero')
elif a < 0:
    print('This is a number smaller than zero')
else:
    print(a == 0)
