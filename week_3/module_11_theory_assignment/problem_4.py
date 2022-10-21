
input_str = input()

output_str = ""

for i, ch in enumerate(input_str) :
    if i % 2 != 0 :
        num_val = int(ch)
        for num in range(num_val) :
            output_str += input_str[i-1]


result_str = "".join(sorted(output_str, key=str.lower))
print(result_str)
