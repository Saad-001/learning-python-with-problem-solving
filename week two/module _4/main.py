# optional parameter in function

def add(num1, num2=5) :
    res = num1 + num2
    print(res)

add(5)

# defining randomly parameters values while calling the function

def print_numbers(num1, num2, num3) :
    print(f'num1 : {num1}, num2 : {num2}, num3 : {num3}')

print_numbers(num3=10, num1=3, num2=5)

# take all arguments using single parameter
 
def multiply(*numbers) :
    result = 1
    for num in numbers :
        result *= num
    return result

output = multiply(1, 2, 3, 4, 5)
print(output)

# taking key value pair arguments

def print_name(f_name, l_name, **knames) :
    print(f_name, l_name, knames)

print_name(f_name="Mr. ", l_name="abdur rahman ", family_name="chowdhury")


def total_cost(price, quantity) :
    cost = price * quantity
    return cost

pay = total_cost(3, 10)
print(f"please pay : {pay}")
