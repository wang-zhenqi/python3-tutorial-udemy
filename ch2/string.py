a = "test"
b = 'This is \'TEST\''

# access a character of string - index
print(a[0])
print(a[-2])
print(len(a))

c = 'abc'
print(c * 5)

name = 'python'
age = 27
new_str = "I'm " + name + ", " + "and " + str(age) + " years old."
print(new_str)

new_str1 = "I'm %s, and %d years old." % (name, age)
print(new_str1)

new_str2 = "I'm {N}, and {A} years old.".format(
        N=name,
        A=age
        )
print(new_str2)

new_str3 = f"I'm {name}, and {age} years old."
print(new_str3)
