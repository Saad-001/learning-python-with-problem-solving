# Write a program to create a function show_employee() using the following conditions - 

# 1. It should accept the employee’s name and salary and display both using a f string.
# 2. If the salary is missing in the function call then assign default value 9000 to salary
# 3. If the name is missing then assign a default value anonymous



def show_employee(name = "anonymous", salary = 9000) :
    print(f"employee name is {name} and his salary is {salary}")

show_employee(salary=5000)
