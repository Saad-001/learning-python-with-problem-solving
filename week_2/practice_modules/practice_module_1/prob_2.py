"""
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call. Receive the returned values and print the type. HInts: Please google how to return multiple values from a function in python

"""

def calculation(num1, num2) :
    addition_res = num1 + num2
    subtraction_res = num1 - num2

    return addition_res, subtraction_res

addition_res, subtraction_res = calculation(5, 3)
print(type(addition_res))
print(type(subtraction_res))
