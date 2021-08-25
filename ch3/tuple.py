# create a tuple
a = (1, 2, 3)
b = 1,

print(a, type(a))
print(b, type(b))

# access items of tuple
print(a[2])
print(a[0:])
print(a[-2])

# tuple functions
tuple1 = (9, 1, -4, 3, 7, 11, 3)
print("length of tuple1 is", len(tuple1))
print("max item of tuple1 is", max(tuple1))
print("min item of tuple1 is", min(tuple1))
print("\'3\' appeared {} times".format(tuple1.count(3)))

# cannot change, reverse or sort a tuple
