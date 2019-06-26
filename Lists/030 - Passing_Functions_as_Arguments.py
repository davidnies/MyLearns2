# https://www.youtube.com/watch?v=Fg-tuFbCSy0&list=PLDoG9_gnmpXe8rZfrSsnseglCJmyKmzi-&index=22

# passing one function as an argument to another function
def add(a, b):
    return a + b

def square(c):
    return c * c

result = square(add(2, 3))
print(result)