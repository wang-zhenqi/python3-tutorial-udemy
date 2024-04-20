This repo contains the practicing source code when I learning Python on a Udemy lecture provided by Xiao Peng.

Here is the learning note that I think is worth keeping. It might not be systematic, but contains some key points that
are easily forgotten.

# Chapter 1 - Get to Know Python

## Website

The official python website: [python.org](python.org).

## Version

Python 2 is so much different from python 3, so before writing the program, choose a proper version.

For practice, we can choose the **second latest version**, because it is stable and contains enough new features.

We can install plenty of versions of python on the same machine. It is common that we use a different version for a
different program. That's why we need a run-time version manager. Usually, `pipenv` is a good choice, it provides a
virtual run-time environment for a specific program so that the program can be isolated from others.

But now, I'm used to using another tool called [`asdf`](http://asdf-vm.com/), it's more convenient to operate. Also, it
gives users a unified way of setting the run-time environment for many languages.

# Chapter 2 - Basic Types

## Indentation

Either `space` or `tab` as long as use the same rule of indentation. **4-spaces** is recommended.

## Data type

Python doesn't define a data type strictly, you can easily change the value of a variable from one type to another:

```python
a = 1
a = 3.14
a = True
a = [1, 2, 3]
```

### Basic types

|  Type   | Sub-type | Example                                                  | Operation                                                       | Comment   |
|:-------:|:--------:|----------------------------------------------------------|-----------------------------------------------------------------|-----------|
| Numbers | Integer  | 123, -23, 0, 0b101, 0x3AD, 0o37, 0b1111_1111 (4095), ... | `+`, `-`, `*`, `/`, `//` (inter division), `**` (exponent), `%` |           |
|         |  Float   | 43.5, -65.222, 1.0, 1.2E3, ...                           | `+`, `-`, `*`, `/`, `//` (inter division), `**` (exponent), `%` |           |
|         | Complex  | 1+2J, 3+5j, ...                                          |                                                                 |           |
| Boolean |          | True, False                                              | `and`, `or`, `not`                                              |           |
|  None   |          | None                                                     |                                                                 |           |
| String  |          | "abc", 'hello world', '', "Tom's hat"                    | `+`, `*`, `in`                                                  | Immutable |

## Strings

### Functions

See [this site](https://www.w3schools.com/python/python_ref_string.asp) for reference.

### Indexing

```python
a = "python"
print(a[0])  # 'p'
print(a[-2])  # 'o'
```

### Slicing

```python
a = "python"
print(a[2:4])  # "th"
print(a[-6:-4])  # "py"
print(a[0:-3])  # "pyt"
print(a[:-2])  # "pyth"
print(a[1:])  # "ython"
```

### Concatenating and Multiplying

```python
a = "py" + "thon"  # "python"
b = (a + ' ') * 3  # "python python python "
```

### Formatting

```python
# "I'm python, and 27 years old."

name = 'python'
age = 27
s1 = "I'm " + name + ", " + "and " + str(age) + " years old."
print(s1)

s2 = "I'm %s, and %d years old." % (name, age)
print(s2)

s3 = "I'm {N}, and {A} years old.".format(
    N=name,
    A=age
)
print(s3)

s4 = f"I'm {name}, and {age} years old."
print(s4)
```

## Floating operations

```python
a = 0.3 / 0.1
print(a)  # It's not 3, 2.9999999999999996 instead

# Similar cases:
# 0.2 + 0.1 = 0.30000000000000004
```

See [here](https://docs.python.org/3/tutorial/floatingpoint.html) to learn why these cases happen.

# Chapter 3 - List and Tuple

## List

A list is like an array in other languages, it contains none or multiple items. But the list in Python is more flexible,
the items are not necessarily required to be the same type. They can be any type - including another list.

### Create a list

Belows are the ways to define a list:

```python
a = [1, 2, 3]
b = [1, 'abc', 2.0, ['a', 'b', 'c']]
```

### Access the items in a list

We can use index to access the items:

```python
a = [1, 2, 3]
print(a[0], a[-1], a[0:2], a[-3:-1], sep=', ', end='***\n')
```

As it shows, the list also has operations like slicing.

### Functions of list

* **Number** of appearance of a certain item: `listA.count(3)`
* **Append** a new item: `listA.append('a')`
* **Insert** an item to a certain position: `listA.insert(1, 'b')`, which mean insert item 'b' to position 1.
* **Delete** an item: `listA.remove('e')`, which remove the first 'e' in the list.
    * If you want to remove the item on certain position, use `pop()`: `listA.pop(3)`
* **Modify** an item: use the index directly, `listA[2] = 'e'`
* **Reverse** a list: `listA.reverse()`
* **Sort** the items in a list: `listA.sort(reverse=[True|False])`, default order is increasing.

## Tuple

A tuple can be considered as a static list. Once a tuple is defined, **the items in it cannot be changed**. This feature
is called **immutable**.

### Create a tuple

Just like creating a list, but use "`[]`" instead:

```python
a = (1, 2, 3)
b = 1,
```

### Access items in a tuple

Same as lists, strings, and so on.

```python
a = (1, 2, 3)
print(a[2], a[0:], a[-2])
```

### Functions of tuple

* **Number** of appearance of a certain item: `tupleA.count(3)`

# Chapter 4 - Dictionary and Set

## Dictionary

A dictionary is similar to a map in another language like Java. The elements in dict are key-value pairs.

As usual, the type of keys or values can all be various. For values, they can be whatever types you like, but for keys,
only **hashable** type is legit.

### Hashable object

> In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not
> change during its lifetime. This allows Python to create a unique hash value to identify it, which can be used by
> dictionaries to track unique keys and sets to track unique values.
>
> -- [stack overflow](https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python#:~:text=In%20Python%2C%20any%20immutable%20object,sets%20to%20track%20unique%20values.)

What's more, a hashable object doesn't mean to be immutable, because you can define a class and make it hashable, but
the object of this class could definitely be changeable.

If you want to test whether an object is hashable or not, you can use `hash()` function, no error occurring means it's
hashable.

### Create a dictionary

```python
a = {
    1: 'a',
    2: 'b',
    '3': 'c',
    4.0: ('d', 'e', 'f')
}

b = dict()  # it's an empty dict

c = dict(a=1, b=2, c='a')
# keep in mind that the keys are strings:
# {'a': 1, 'b': 2, 'c': 'a'}
```

### Access the items in a dictionary

1. Get values by keys

   ```python
   a = dict(a = 1, b = 2, c = 'a')
   print(a['c'])
   ```

2. Get values by `get()`

   ```python
   d = {
     'Name': 'Jack',
     'Age': 9,
     'Grade': 5
   }
   print(d.get('Age'), d['Name'], d.get('None'))
   # 9 Jack None
   ```

### Update/add items

If the key exists, update its value, if not, add a new key-value pair.

```python
d['Name'] = 'Tom'
c = dict(Sex='Male', ID='1100101', Age=12)
d.update(c)
# {'Name': 'Tom', 'Age': 12, 'Grade': 5, 'Sex': 'Male', 'ID': '1100101'}

b = {**c, **d}
# {'Sex': 'Male', 'ID': '1100101', 'Age': 12, 'Name': 'Tom', 'Grade': 5}
```

### Functions of dict

```python
d.keys()  # returns the dict_keys type data
d.values()  # returns the dict_values type data
d.items()  # returns the dict_items type data
d.pop('Name')  # remove the key-value pair
```

## Set

We can treat a set as a dict without value. The items in a set are **distinct**, with no duplication.

From this, we can deduct that the data structure behind the scene is also the hash table, so that the items of a set
should also be **hashable**.

### Create a set

Similar to creating a dict, use curly brackets: `a = {'a', 'b', 'c'}`

Or you can use set():

```python
l = [1, 2, 3, 4, 5]
s = set(l)
# if the list l has duplicated items, after calling set(), it will be reduced to only 1.
```

### Function of set

```python
s = {3, 4, 5, 6}
s.add(7).  # {3, 4, 5, 6, 7}
s.remove(5)  # {3, 4, 6, 7}

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# operation of set
print(s1 & s2)  # intersection: {3, 4}
print(s1 | s2)  # union: {1, 2, 3, 4, 5, 6}
print(s1 ^ s2)  # symmetric difference: {1, 2, 5, 6}
print(s1 - s2)  # difference: {1, 2}
```

# Chapter 5 - Branch and Loop Statements

Since this part is not very hard to understand, nor to remember, I don't want to keep so many details, just some of the
important points.

## Boolean statements

Boolean statements are statements having values of boolean type, which means the interpreter will evaluate the
statements as either 'True' or 'False'.

Typical boolean statements are as follows:

```python
3 > 5  # False
3 == 9 / 3  # True
3 in range(10)  # True
bool(1 & 0)  # False
a is not b  # It depends
```

## range() function

```python
for item in range(0, 20, 5):
    # range(included start, excluded end, step)
    print(item)
    # 0 5 10 15
```

