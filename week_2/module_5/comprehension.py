numbers  = [12, 45, 65, 23, 89, 78, 11]

odd_numbers = [num for num in numbers if num % 2 == 1 if num % 5 == 0]

print(odd_numbers)

my_string = "something i'm looking"

k = [print(i) for i in my_string if i not in "aeiou"]
