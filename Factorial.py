#  Factorial

def factorial(num):
    i = 1
    factorial_ = 1
    while i <= num:
        factorial_ *= i
        i+=1
    return  factorial_

print(factorial(5))