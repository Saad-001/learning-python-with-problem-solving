"""
Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

Given Tuple:
tuple1 = (11, [22, 33], 44, 55)

Expected Output:
(11, [222, 33], 44, 55)

"""
tuple1 = (11, [22, 33], 44, 55)

for item in tuple1 : 
    if type(item) is list :
        item[0] = 222
  
print(tuple1)
