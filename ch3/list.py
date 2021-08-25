# create a list
a = [1, 2, 3]
b = [1, 'abc', 2.0, ['a', 'b', 'c']]

print(a)
print(b)

# access the item in a list
print(b[0], b[1], sep=', ', end='***\n')

# slice notation
c = b[1:3]
print(type(c), c, sep='\t')

s = 'abcdef'
print(s[1:4], s[-1], s[-2:-1])


# function of list
l = [9, 1, -4, 3, 7, 11, 3]

print('length of l is', len(l))
print('the max item of l is', max(l))
print('the min item of l is', min(l))
print('\'3\' appeared {} times'.format(l.count(3)))

# modification of list
l2 = ['a', 'c', 'd']
# append a new item to l2
l2.append('e')
print(l2)

# insert 'b' between 'a' and 'c'
l2.insert(1, 'b')
print(l2)

# delete 'b' in l2
l2.remove('e')
print(l2)

# change an item
l2[-1] = 'e'
print(l2)

# reverse list
l3 = [1, 2, 3]
l3.reverse()
print(l3)

# sort list items
l4 = [9, 1, -4, 3, 7, 11, 3]
print('l4 =', l4)
l4.sort(reverse=True)
print('l4 =', l4)

