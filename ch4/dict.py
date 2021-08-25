# create a dictionary
a = {
        1: 'a',
        2: 'b',
        '3': 'c'
}
print(a, type(a))

# only hashable type can be the type of key, i.e. int, float, string, char, even tuple...

d = dict()
e = dict(a = 1, b = 2, c = 'a')
print(d)
print(e)

# access items of a dict
print(e['c'])
e['d'] = 123
e['a'] = 'a'
print(e)

d = {
        'Name': 'Jack',
        'Age': 9,
        'Grade': 5,
}
print(d['Name'])
print(d.get('Age'))
print(d.get('None'))

# dict functions
print(d.keys())
print(d.values())
print(d.items())

c = d.pop('Name')
print(c)
print(d)

# update dict
d['Name'] = 'Tom'
c = {
        'Sex': 'Male',
        'ID': '1100101',
        'Age': 12
}
d.update(c)
print(d)

b = {**c, **d}
print(b)

