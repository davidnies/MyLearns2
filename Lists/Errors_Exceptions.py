

# sytax error
def function1(a, b):
    # try block
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Can not divide by Zero! ')

    finally:
        print('this happens even when we have an excption')

# exception - ZeroDivisionError - division by zero

function1(20, 0)





