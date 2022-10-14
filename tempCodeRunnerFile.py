
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
