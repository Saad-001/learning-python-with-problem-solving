"""
6. Complete the following code
def clean_string(text):
    ....
    ....
    print(output)
    
s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)


If you face any errors, fix them. Get help from google. Do not ask others.

"""

def clean_string(text):
    output = ""
    for ch in text :
        if ch.isalpha() :
            output+= ch
    print(output)
    return output


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"    

output = clean_string(s)
print(output)
