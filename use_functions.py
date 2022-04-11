
# type hints don't confuse the runtime, but are *entirely ignored!*
# separate tools can be used to validate the type-integrity of your code
# def add(a: int, b: int) -> int:
def add(a, b = 2):
    # Triple quotes make a multi-line string (in general!!!)
    """
    This is a documentation string
    :param a:
    :param b:
    :return:
    """
    return a + b

print(add("hello", "goodbye"))
print(add(3, 2))
print(add.__doc__)  # I think there's another route to this.

# print(add(1, 2, 3)) # python mandates the right number of posional args

print(add(10))

def show_all(a, b, *args, **kwargs):
    print(f"a is {a} b is {b}")
    print(args)
    for item in args:
        print(f"> {item}")
    print(type(kwargs))
    for k in kwargs:
        print(f"kw: {k} -- {kwargs[k]}")

# positional args come first, varargs (one group of them) second, kwargs last
show_all(1, 2, 3, 4, 5, 6, alfred="King", oddball="Something")

values = ["hello", "goodbye", "whatever"]
show_all("x", "y", *values)
print("---------------")
show_all(*values)

print(add)
print(type(add))

sum = add
print(type(sum))

print(sum(3, 4))

# no parens around formal parameter list
addup = lambda a,b: a + b

print(addup(4,6))

listostuff = [(1, 4), (2, 5), (3, 2), (4, 3)]
print(listostuff)

## FIX THIS SIMON!!!
# listostuff.sort(lambda t: t[1])
print(listostuff)
#  closures do what you would expect

