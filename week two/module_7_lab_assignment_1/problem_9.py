"""
9. You need to make a positive story into a negative by changing some of its words automatically. Someone gave you a list `replace with’ and asked to find the words that are in that list in string ‘s’ and replace them with the next word of that list.

replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."


Output example (one done for you): 
"I am the thief of Baghdad..........."


Write a function named replace_word() and write your code inside this function.

"""
# approach one to solve the above problem

def replace_word() :

    replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

    s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
    
    s_list = s.split(" ")

    for word in s_list :
        for idx, rep_word in enumerate(replace_with) :
            if word == rep_word :
                s = s.replace(word, replace_with[idx+1])

    return s

print(replace_word())

# approach two to solve the above problem 

"""
replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

s_list = s.split(" ")

def replace_word() :

    output_str = ""

    for word in s_list :
        matched = 0
        for idx, rep_word in enumerate(replace_with) :
            if word == rep_word :
                output_str += replace_with[idx+1] + " "
                matched = 1
        if matched == 0 :
            output_str += word + " "

    return output_str

print(replace_word())

"""
