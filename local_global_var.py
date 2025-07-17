x=4
print(x)

def hello():
    global x
    x=5
    print(f"The local variable is {x}")
    print("hello ashish")

print(f"The Global variable iS {x}")
hello()
print(f"The global Varibal is {x}")
