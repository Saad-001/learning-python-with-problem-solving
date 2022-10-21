
class Calculator :
    my_res = 50

    def __init__(self) :
        self.cart = []

    def add (self, num_1, num_2, item) :
        self.cart.append(item)
        res = num_1 + num_2
        return res
    
    def subtract (self, num_1, num_2) :
        res = num_1 - num_2
        return res

    def multiply (self, num_1, num_2) :
        res = num_1 * num_2
        return res

    def devide (self, num_1, num_2) :
        res = num_1 / num_2
        return res


calculation = Calculator()
added_ans = calculation.add(5, 10, "tshirt")
ch = Calculator()
ch_ad = ch.add(3, 3, "shoes")
ch_ad = ch.add(3, 5, "pants")
# subtracted_ans = calculation.subtract(5, 10)
# multiplyed_ans = calculation.multiply(5, 5)
# devided_ans = calculation.devide(10, 2)

# print(added_ans, subtracted_ans, multiplyed_ans, devided_ans)

# print(calculation.cart)
# print(ch.cart)

class People():
    def __init__(self, name):
      self.name = name

    def namePrint(self):
      print(self.name)

person1 = People("Emma")
person2 = People("Watson")
person1.namePrint()

class Person:
    def __init__(self, id):
        self.id = id

    def __call__(self) :
        return self.__dict__

sam = Person(100)
sam.__dict__['age'] = 49

# print (sam.age + len(sam.__dict__))

print(sam())
