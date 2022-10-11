"""
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary
Hints: Search about Dictionary Comprehension

Given dictionary:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

Expected Output:
{'name': 'Kelly', 'salary': 8000}

"""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }

# Keys to extract
keys = ["name", "salary"]

# approach one

new_dict = {}

for key in sample_dict : 
    if key == "name" or key == "salary" :
        new_dict[key] = sample_dict[key]

print(new_dict)

# approach two using dictionary comprehension

new_dict_2 = {key : value for (key,value) in sample_dict.items() if key == "name" or key == "salary"}

print(new_dict_2)

