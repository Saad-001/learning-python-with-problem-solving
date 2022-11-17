"""
2. Write a program center_align.py to centre align all lines in the given file.
Example output: 

                                        I am sure that the shells are seashore shells. 
                                        So if she sells seashells on the seashore, 
                                        The shells that she sells are seashells, 
                                        I am sure She sells seashells on the seashore;

"""

line1 = "I am sure that the shells are seashore shells."
line_2 = "So if she sells seashells on the seashore,"
line_3 = "The shells that she sells are seashells,"
line_4 = "I am sure She sells seashells on the seashore;"
str_list = [line1, line_2, line_3, line_4]

for i in range(len(str_list)) :
    print(f"{str_list[i].center(130)}")

