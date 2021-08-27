# python3-tutorial-udemy
> This repo contains the practicing source code when I learning Python on a Udemy lecture provided by Xiao Peng.

Here is the learning note that I think is worth keeping. It might not be systematic, but contains some key points that are easily forgotten.



## Chapter 1

### Website

The official python website: [python.org](python.org).

### Version

Python 2 is so much different from python 3, so before writing the program, choose a proper version.

For practicing, we can choose the **second latest version**, because it is stable and contains enough new features.

We can install plenty of versions of python on the same machine. It is common that we use a different version for a different program. That's why we need a run-time version manager. Usually, `pipenv` is a good choice, it provides a virtual run-time environment for a specific program so that the program can be isolated from others.

But now, I'm used to using another tool called [`asdf`](http://asdf-vm.com/), it's more convenient to operate. Also, it gives users a unified way of setting the run-time environment for many languages.



## Chapter 2

### Indentation

Either `space` or `tab`, as long as use the same rule of indentation. **4 spaces** is recommended.



### Data type

Python doesn't define a data type strictly, you can easily change the value of a variable from one type to another:

```python
a = 1
a = 3.14
a = True
a = [1, 2, 3]
```



#### Basic types

|  Type   | Sub-type | Example                                                  | Operation                                                    | Comment   |
| :-----: | :------: | -------------------------------------------------------- | ------------------------------------------------------------ | --------- |
| Numbers | Integer  | 123, -23, 0, 0b101, 0x3AD, 0o37, 0b1111_1111 (4095), ... | `+`, `-`, `*`, `/`, `//` (inter division), `**` (exponent), `%` |           |
|         |  Float   | 43.5, -65.222, 1.0, 1.2E3, ...                           | `+`, `-`, `*`, `/`, `//` (inter division), `**` (exponent), `%` |           |
|         | Complex  | 1+2J, 3+5j, ...                                          |                                                              |           |
| Boolean |          | True, False                                              | `and`, `or`, `not`                                           |           |
|  None   |          | None                                                     |                                                              |           |
| String  |          | "abc", 'hello world', '', "Tom's hat"                    | `+`, `*`, `in`                                               | Immutable |



### Strings

#### Functions

See [this site](https://www.w3schools.com/python/python_ref_string.asp) for reference.



#### Indexing

```python
a = "python"
print(a[0])		# 'p'
print(a[-2])	# 'o'
```



#### Slicing

```python
a = "python"
print(a[2:4])		# "th"
print(a[-6:-4]) # "py"
print(a[0:-3])	# "pyt"
print(a[:-2])		# "pyth"
print(a[1:])		# "ython"
```



#### Concatenating and Multiplying

```python
a = "py" + "thon"		# "python"
b = (a + ' ') * 3		# "python python python "
```



#### Formatting

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



### Floating operations 

```python
a = 0.3 / 0.1
print(a)	# It's not 3, 2.9999999999999996 instead

# Similar cases:
# 0.2 + 0.1 = 0.30000000000000004
```



See [here](https://docs.python.org/3/tutorial/floatingpoint.html) to learn why these cases happen.

