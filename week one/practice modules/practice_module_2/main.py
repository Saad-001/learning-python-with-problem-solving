# problem 1 and solution

"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.(don’t use any python built in function)
Example :  pHitrOn.iO presents "Python COuRSe".
Ans : PhITRoN.Io PRENSENTS “pYTHON coUrsE”

"""

str = input("Enter a string : \n")

outPut_str = ""

for character in str : 
    if character >= 'a' and character <= 'z' :
        outPut_str += chr(ord(character) - 32)
    elif character >= 'A' and character <= 'Z' :
        outPut_str += chr(ord(character)  + 32)
    else :
        outPut_str += character

print(outPut_str);

# problem 2 and solution

"""
Write a program to print the following number pattern using a loop.
Input : 5
Output : 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""

num = int(input("Enter a number : \n"))

for count in range(num + 1) :
    for count2 in range(1, count+1) :
        print(count2, end = " ") 
    print("\n")

# problem 3 and solution

# Display Fibonacci series up to 10 terms

fibo_1 = 0
fibo_2 = 1
count = 0
next_fibo = 0

while count < 10 :
    if count < 2 :
        print(count, end = " ")
    else:
        next_fibo = fibo_1 + fibo_2
        fibo_1 = fibo_2
        fibo_2 = next_fibo
        print(next_fibo, end = " ")
    count+=1

# problem 4 and solution

"""
Count all uppercase, lowercase, digits, and special symbols from a given
"P@#yn26at^&i5ve"
Total counts of chars, digits, and symbols 

Uppercase = 1
Lowercase = 7 
Digits = 3 
Symbol = 4

"""

str = "P@#yn26at^&i5ve"

upperCase = 0
lowerCase = 0
digits = 0
symbols = 0

for i in range(len(str)) :
    if  str[i].islower() :
        lowerCase+=1
    elif  str[i].isupper() :
        upperCase+=1
    elif  str[i].isdigit() :
        digits+=1
    else :
        symbols+=1

print(f"UpperCase = {upperCase}")
print(f"LowerCase = {lowerCase}")
print(f"digits = {digits}")
print(f"Symbols = {symbols}")


# problem 5 and solution

"""
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1 = "Abc"
s2 = "Xyz"

Output : AzbycX

"""

s1 = "Abc"
s2 = "Xyz"
total_len = len(s1) + len(s2)
idx_s1 = 0
s2_len = len(s2)
idx_s2 = s2_len - 1

output_s = ""

for i in range(total_len) :
    if idx_s1 < len(s1) :
        output_s += s1[idx_s1]
        idx_s1+=1
    
    if idx_s2 >= 0 :
        output_s += s2[idx_s2]
        idx_s2-=1

print(output_s)

# problem 6 and solution

"""
Write a program to check if one string contains another. For example, the result will be True if all the characters in the s1 are present in s2, otherwise False. The character’s position doesn’t matter. Take inputs from the user.

s1 = "Phi"
s2 = "Phitron"

Output : True

"""
s1 = input("Enter the sub string you want to check : \n")
s2 = input("Enter the full string : \n")

is_present = False

for i in range(len(s1)) :
    for j in range(len(s2)):
        if s1[i] == s2[j] :
            is_present = True
            break

        is_present = False
    
    if is_present == False :
        break

if is_present :
    print("True")
else : 
    print("False")


# write a programe to check if the given number is a palindrome number

input_num = input("Enter your number \n")
idx = 0

is_palindrome = False

for i in range(len(input_num) -1, -1 , -1) :
    if input_num[i] == input_num[idx] :
        is_palindrome = True
        idx+=1
        continue

    is_palindrome = False
    break

if is_palindrome :
    print("True")
else :
    print("False")

# problem 8 and solution

"""
Write a program to display all prime numbers within a range. You will be given two integers l and r . You have to print all the prime numbers present in the given range l and r.
Input : 25 50

Output :
29
31
37
41
43
47

"""

for n in range(25, 50) :
    is_prime = False
    for devider in range(2, 25) :
        if n % devider == 0 :
            is_prime = False
            break
        is_prime = True
    
    if is_prime :
        print(n)


# problem 9 and solution

# Reverse a given integer number

inp_num_str = input("Enter number to reverse : \n")
inp_num = int(inp_num_str);

for n in range(len(inp_num_str)-1, -1, -1) :
    print(inp_num_str[n], end = "")
