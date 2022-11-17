
# def replace_word() :

#     replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

#     s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
    
#     s_list = s.split(" ")

#     for word in s_list :
#         for idx, rep_word in enumerate(replace_with) :
#             if word == rep_word :
#                 s = s.replace(word, replace_with[idx+1])

#     return s

# print(replace_word())

# class Demo:
#     def check(self):
#         return "Demo's check "
#     def display(self):
#         print(self.check(),end="")
# class Demo_Derived(Demo):
#     def check(self):
#         return "Derived's check "
# Demo().display()
# Demo_Derived().display()

# class A:
#     def one(self):
#         return self.two()
#     def two(self):
#         return 'A'
# class B(A):
#     def two(self):
#         return 'B'
# obj1=A()
# obj2=B()
# print(obj1.two(),obj2.two())

# class Demo:
#     def __check(self):
#         return "Demo's check "
#     def display(self):
#         print(self.__check(),end="")
# class Demo_Derived(Demo):
#     def __check(self):
#         return "Derived's check "
# Demo().display()
# Demo_Derived().display()

# class A:
#     def test(self):
#         print("Test of A is called ",end="")
# class B(A):
#     def test(self):
#         print("Test of B is called ",end="")
#         super().test()
# class C(A):
#     def test(self):
#         print("Test of C is called ",end="")
#         super().test()
# class D(B,C):
#     def test2(self):
#         print("Test of D is called ",end="")
# obj=D()
# obj.test()

# class A:
#     def __init__(self) -> None:
#         self.multiply(15)
#         print(self.i)
#     def multiply(self,i):
#         self.i=4*i
# class B(A):
#     def __init__(self) -> None:
#         super().__init__()
#     def multiply(self, i):
#         self.i=2*i
# obj=B()

# a=False
# while not a:
#     try:
#         f_n = input("Enter file name")
#         i_f = open(f_n, 'r')
#     except:
#         print("Input file not found")