
x = 20
y = 100
if x > y:
    print("x is bigger!")
elif x > (y // 2):
    print("It's small, but not tiny")
else:
    print("x is a lot smaller")
    print("oh, what?")

message = "Modest" if x < 100 else "big"
print(message)

# unless you're using Python 3.10 there is no "switch/case"
# 3.10 introduced "match"

match x:
    case 20: print("it's twenty")
    case 30: print("it's 30")
    case _: print("it's something else")  # equivalent to "default"

# tup = ("Hello", "Bonjour")
# tup = 10
tup = ["hello", 314]
match tup:
    # guard condition--ensure potential ambuguity is resolved with ORDER
    # first match wins!!!
    case (x, y) if y < 4: print(f"it's a with small y x is {x}, y is {y}" )
    case (x, y): print(f"it's a tuple x is {x}, y is {y}" )
    case 10: print("it's a number ten")

