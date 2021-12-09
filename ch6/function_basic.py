# define a function
def demo():
    print('Hello demo')

def demo1(a, b):
    print(a, b)

def sum(a, b):
    return a + b

def my_max(a):
    if not a:
        return None

    max_item = a[0]

    for i in a:
        if max_item < i:
            max_item = i

    return max_item

demo()
demo1(a = [1, 2, 3], b = {1: 'a', 2: 'b'})
print(sum([1, 2, 3], [4, 5, 6]))

lists = [[], [3], [5, 2, -4, 3, 5, 1, 6]]

for i in range(3):
    print(my_max(lists[i]))

