
names = {"Fred": "Jones"}

try:
    print(names["Fred"])
    print("is that helpful")
    # "with" ensures the resource is closed reliably, exception or not!!!
    with open("text.txt", "r") as input:
        for line in input:
            print("> " + line)  # line includes the line-ending (if there was one)
        print("end of file")
except KeyError as ke:
    print(f"oops, not found, got {ke}")
except FileNotFoundError as fnfe:
    print(f"bother file not found {fnfe}")
finally:
    print("carrying on...")

print("rest of file")