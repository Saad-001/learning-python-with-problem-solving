"""
7. Write a program to display a simple form of digital book. “Books” are text files in which each block (page) of text is followed by a double dash (--). When a book is displayed, the first block of text is shown and the program should wait for the user to press the enter key before displaying the next.

File.txt:
This is first page content--Now we are in the second pageq


Output:
This is first page content
[enter - read more, press q to quit]

"""

global idx
idx = 0

while True :
    with open("file.txt", "r") as file :
        data = file.read()
        text = data.split("--")
        len_of_text = len(text)
        if idx == 0 :
            print(text[idx])
    choice = input("[Enter - to read more, press q to quit] : ")
    if choice == "q" :
        file.close()
        break
    elif choice == "" :
        idx+=1
        if idx < len_of_text :
            print(text[idx])
        else :
            print("You have read the whole book.")
    else :
        print("Invalid input")

