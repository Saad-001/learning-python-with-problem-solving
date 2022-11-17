def my_func (func) :
    print("start my func")
    res = func(5, 3)
    print("end my func")
    print(res)
    # return func

@my_func
def add (num_1, num_2) :
    return num_1 + num_2



# res = my_func()
# print(res)
