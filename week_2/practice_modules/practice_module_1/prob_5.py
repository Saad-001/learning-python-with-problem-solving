"""
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
Hints: Search about dict() function

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

ziped_output = zip(keys, values)
new_list = list(ziped_output)

# approach one
my_dict_1 = {}

idx = 0
for elem in new_list :
    my_dict_1[elem[idx]] =  elem[idx+1]

# approach two 
my_dict_2 = dict(new_list)

print(my_dict_1)
print(my_dict_2)
