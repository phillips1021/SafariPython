
x = 5
while x > 0:
    print(f"x is {x}")
    x -= 1  # no ++ or --
print("all done")

# Python does not have "do while"

# numbers = list(range(1, 10))
numbers = range(1, 10)
print(numbers)
for x in numbers:  #  iterates iterator, many things are iterator, list, dict, set
    print(f"x is {x}")

print("all done again")

for x in "Hello":
    print(x)

names = {"Fred": "Jones", "Alan": "Smith"}
for n in names:  # iterates keys
    print(n, " lastname is", names[n])

for ln in names.items():
    print(ln[0], "last is", ln[1])

print("----------------------------")

x = 0
while x < 5:
# if x < 5:
    print(x)
    x += 1
    # if x == 3:
    #     break
else:
    print("What are we doing here?")

