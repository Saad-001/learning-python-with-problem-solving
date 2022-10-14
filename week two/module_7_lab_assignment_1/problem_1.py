"""
1. Create a string out of some words given in a list -

l = ["This", "is", "very", "fantastic"]


Expected Output:
"This is very fantastic"

Write a function named create_string() and write your code inside this function.

"""

def create_string() :
    given_list = ["This", "is", "very", "fantastic"]

    output_str = ""
    for word in given_list :
        output_str += word + " "

    print(output_str)

create_string()
