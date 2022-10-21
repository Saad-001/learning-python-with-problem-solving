"""
3. Go to this repo: https://pypi.org/project/pyjokes/ and try to make a chat bot to tell you joke using pyjokes.
Write a function named tell_some_jokes() and write your code inside this function.

"""
import time

import pyjokes


def tell_some_jokes() :
    print("hey man... you're looking bored!")
    print("wanna hear some jokes? y/n : ")
    
    ans = input()
    jokes_count = 0

    while ans == "y" :
        if jokes_count == 0 :
            print("tell me what kind of jokes do you love?")
            time.sleep(1)
            print("I know three kinds of jokes.")
            time.sleep(1)
        print("choose one of them you'd love to hear.")
        time.sleep(1)
        print("neutral / chuck / all")
        choice = input()
        if choice == "neutral" or choice == "chuck" or choice == "all" :
            joke = pyjokes.get_joke('en', choice)
            if jokes_count == 0 :
                print(f"let me tell you a joke 😃: {joke}")
            else :
                print(f"let me tell you another joke 😃: {joke}")
        else :
            while choice != "neutral" or choice != "chuck" or choice != "all" :
                print("please choose one of the mentioned jokes.")
                choice = input()
                if choice == "neutral" or choice == "chuck" or choice == "all" :
                    joke = pyjokes.get_joke('en', choice)
                    if jokes_count == 0 :
                        print(f"let me tell you a joke 😃: {joke}")
                    else :
                        print(f"let me tell you another joke 😃: {joke}")
                    break
                
        jokes_count+=1
        time.sleep(5)
        print("")
        print("wanna hear more jokes? y/n : ")
        ans = input()
            
    if(ans == "n" and jokes_count == 0) :
        print("I'm sorry! I couldn't make you laugh.")
        return


tell_some_jokes()
