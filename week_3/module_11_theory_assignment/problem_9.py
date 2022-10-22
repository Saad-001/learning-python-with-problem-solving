class My_class:

    def __init__(self, x, n):
        self.X = x
        self.n = n

    def sum (self) :
        return self.X + self.n

    def pow (self) :
        return self.X ** self.n


instance_1 = My_class(2, 3)

sum_result = instance_1.sum()
pow_result = instance_1.pow()

print(sum_result, pow_result)
