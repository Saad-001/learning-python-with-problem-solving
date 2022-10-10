import time

import pyautogui

pyautogui.alert('This is an alert box from saad.')

name = pyautogui.prompt('What is your name?')
print(name)

opt = pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
print(opt)

password = pyautogui.password('Enter password (text will be hidden)')
print(password)

for i in range(1, 5) :
    time.sleep(5)
    if i == 1 :
        pyautogui.write("Hi farhan !")
        pyautogui.press("enter")
    elif i == 2 :
        pyautogui.write("How are you ?")
        pyautogui.press("enter")
    elif i == 3 :
        pyautogui.write("I love python")
        pyautogui.press("enter")
    elif i == 4 :
        pyautogui.write("now I'm texting you automatically using python")
        pyautogui.press("enter")
    else :
        break
    
