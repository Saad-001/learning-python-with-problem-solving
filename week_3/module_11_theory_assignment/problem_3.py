input_str = input().split(" ")

output_str = ""

for word in input_str :
    output_str += word[::-1] + " "

print(output_str)

