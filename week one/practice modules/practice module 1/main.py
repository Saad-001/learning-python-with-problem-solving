import math

# Problem 1

# Suppose you have a floating number N.1 then,
# Floor is the greatest integer less than or equal to N. And Ceil is the smallest
# number greater than or equal to N.
# Example: for 3.4 Floor is 3 and Ceil if 4.

# Problem 1 solution

num = float(input('Enter a floating number : '))
floor_form = math.floor(num)
ceil_form = math.ceil(num)

print(f'for {num} Floor is {floor_form} and Ceil is {ceil_form}')

# Problem 2

# Write a function that takes 3 integer inputs from user and
# outputs absolute values of these integers without using any
# library functions.

# Problem 2 solution

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < 0 :
    num1*= -1
else :
    num1 = num1

if num2 < 0 :
    num2*= -1
else :
    num2 = num2

if num3 < 0 :
    num3*= -1
else :
    num3 = num3

print(num1, num2, num3)

# Problem 3

# In the famous Rock Paper Scissor game - Rock wins against scissors, paper wins
# against rock, and scissors wins against paper.
# Write a python program that takes two user inputs and returns who wins the game.
# Sample Input:
# > Player 1: rock
# > Player 2: paper
# Sample Output:
# > Player 2 is the winner

# Problem 3 solution

player_1 = input("Enter player 1 (rock/scissor/paper) : ")
player_2 = input("Enter player 2 (rock/scissor/paper) : ")

if player_1 == 'rock' and player_2 == 'scissor' :
    print('Player 1 is the winner')
elif player_1 == 'scissor' and player_2 == 'rock' :
    print("Player 2 is the winner")
elif player_1 == 'rock' and player_2 == 'paper' :
    print("Player 2 is the winner")
elif player_1 == 'paper' and player_2 == 'rock' :
    print("Player 1 is the winner")
elif player_1 == 'scissor' and player_2 == 'paper' :
    print("Player 1 is the winner")
elif player_1 == 'paper' and player_2 == 'scissor' :
    print("Player 2 is the winner")

# Problem 4

# Write a Python program to check if user entered number is ZERO, POSITIVE or
# NEGATIVE until user does not want to quit.
# User will type ‘Quit’ to close the program.
# Sample:
# > Enter input: 2
# > 2 is positive
# > -3
# > -3 is negative
# > “Quit”
# > (stop the program)

# Problem 4 solution

exit = False

while(exit != True) :
    data = input()
    if data != "Quit" :
        if int(data) < 0 :
            print(f'{data} is negative')
        elif int(data) == 0 :
            print(f'{data} is Zero')
        else :
            print(f'{int(data)} is positive')
    else :
        print("program stopped")
        exit = True

# Problem 5

# Write a Python program which iterates the integers from 1 to 50. For multiples of three
# print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers
# which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

# Problem 5 solution

for num in range(50) :
    if num % 3 == 0 and num % 5 == 0 :
        print("fizzbuzz")
    elif num % 3 == 0 :
        print("fizz")
    elif num % 5 == 0 :
        print("buzz")
    else :
        print(num)
