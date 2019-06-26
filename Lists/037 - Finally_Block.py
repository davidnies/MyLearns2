# https://www.youtube.com/watch?v=zW3z3h4ssi4&list=PLDoG9_gnmpXe8rZfrSsnseglCJmyKmzi-&index=26

try:
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    print('Can not divide by Zero! ')

finally:
    print('this happens even when we have an excption')
