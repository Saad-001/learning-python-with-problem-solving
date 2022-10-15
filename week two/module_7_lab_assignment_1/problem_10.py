"""
10. Given a string ‘s’ you need to find the words that are in list ‘a’ and use the next words on string ‘s’ to create a new string. Save it inside a file called ‘out.txt’. Remember to close the file after writing.

Write a function named create_new_string() and write your code inside this function.

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

output = "I love Bangladesh" (inside a file)

"""
import string

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

new_string = s.translate(str.maketrans('', '', string.punctuation))

s_list = new_string.split(" ")

output_str = ""

to_word_count = 0

for word in a :
    for i,s_word in enumerate(s_list) :
        if word.lower() == s_word.lower() :
            if word.lower() == "to" :
                to_word_count+=1
                if to_word_count <= 1 :
                    continue
            output_str+= s_list[i+1] + " "


file = open("out.txt", "a")
file.write(f"{output_str}")
file.close()

