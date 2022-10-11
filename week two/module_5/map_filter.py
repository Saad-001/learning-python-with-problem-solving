numbers = [1, 2, 3, 4, 5]

double_it = lambda x : x * 2

filter_it = lambda x : x % 2 == 0

doubled_numbers = list(map(double_it, numbers))

filtered_numbers = list(filter(filter_it, numbers))

# print(doubled_numbers)
print(filtered_numbers)
