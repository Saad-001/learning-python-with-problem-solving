a, n = input("Enter two numbers : ").split(" ")


def exp(a, n) :
    num_1 = int(a)
    num_2 = int(n)
    return pow(num_1, num_2)

result = exp(a, n)
print(result)
