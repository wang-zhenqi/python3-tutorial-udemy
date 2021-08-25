a = 'abcdef'
for ch in a:
    print(ch)

b = [1, 2, 3, 4]
c = ('x', 'y', 'z')
d = {
        1: 'a',
        2: 'b',
        3: 'c'
}
e = {1, 2, 3, 5, 9}
for item in d:
    print(item)

for item in range(0, 20, 5):
    # range(included start, excluded end, step)
    print(item)
