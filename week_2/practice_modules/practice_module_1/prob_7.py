"""
We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
Write a Python program to check if value 100 exists in the following dictionary. If it is present print “present” otherwise print “not present”

Sample Dictionary:
sample_dict = {'a': 100, 'b': 200, 'c': 300}

Expected Output:
present

"""

sample_dict = {'a': 300, 'b': 200, 'c': 100}

found = False

for key,value in sample_dict.items() :
    if value == 100 :
        print("present")
        found = True
        break

if(found == False) :
    print("not present")
