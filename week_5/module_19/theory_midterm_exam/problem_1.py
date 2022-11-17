"""
1. We can read 'abba' if we reverse the letters, it’s still 'abba', so this string is called palindrome. Write a python program to check if a string is palindrome or not. 

"""

input_str = "abba"
len_str = len(input_str)
output_str = ""

for i in range(len_str, 0, -1) :
    output_str += input_str[i-1]

if input_str == output_str :
    print("palindrome")
else :
    print("not palindrome")
