# https://www.youtube.com/watch?v=0731gkTw2Ho&list=PLDoG9_gnmpXe8rZfrSsnseglCJmyKmzi-&index=25


def function1(a, b):
    # try block
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Can not divide by Zero! ')


# exception - ZeroDivisionError - division by zero

function1(20, 0)


