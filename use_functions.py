
# type hints don't confuse the runtime, but are *entirely ignored!*
# separate tools can be used to validate the type-integrity of your code
# def add(a: int, b: int) -> int:
def add(a, b):
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

print(add(1, 2, 3)) # python mandates the right number of posional args

# default value for args, variable length args, keyword args
# lambdas
# exceptions, IO, classes