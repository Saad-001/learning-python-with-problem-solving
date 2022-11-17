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
    if choice.isalpha() and choice != "q" :
        print("Invalid input")
        continue
    if choice == "q" :
        file.close()
        break
    elif choice == "" :
        idx+=1
        if idx < len_of_text :
            print(text[idx])
        else :
            print("You have read the whole book.")
    elif choice.strip().isdigit() :
        if (int(choice)) < len_of_text :
            idx = idx + int(choice)
            print(text[idx])
        else :
            print(f"this {choice} number page is not available in the book")
    elif int(choice) < 0 :
        print(text[idx + int(choice)])
        idx = idx + int(choice)