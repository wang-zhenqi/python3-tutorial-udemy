# create a set (a dict without value)
a = {'a', 'b', 'c'}
print(a, type(a))

print('d' in a)

l = [1, 2, 3, 2, 4, 5, 2]
s1 = set(l)
print('s1:', s1)

d = dict()
for i in l:
    if not d.get(i):
        d[i] = 1
s2 = set(d.keys())
print('s2:', s2)

# set functions
s = {3, 4, 5, 6}
s.add(7)
s.add(5)
s.remove(5)
print('s:', s)

print(s & s1)
print(s | s1)
print(s ^ s1)
print(s - s1)
