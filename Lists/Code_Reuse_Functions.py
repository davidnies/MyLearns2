# defining a function and calling it.
def function1():
    print("ashutosh")
    print("apple")
    print("new york")

function1()

# Passing arguments to a function
def add(a,b):
    print(a * b)

add(10,20)


# Returning value from a function
def add(a, b):
    c = a + b
    return c

result = add(100, 200)
print(result)

# passing one function as an argument to another function
def add(a, b):
    return a + b

def square(c):
    return c * c

result = square(add(2, 3))
print(result)