# WARNING --> A large amount of messages can crash your computer.
# CREDITS --> This code is written by Berard on BreachForums.

import time
import pyautogui  # Importing libraries

msg = input("Enter the message -->")
n = input("How many times -->  ")

count = 5

while count != 0:
    print(count)
    time.sleep(1)  # You can edit the speed of the messages.
    count -= 1

print("kilob is arriving!")
for i in range(0, int(n)):
    pyautogui.typewrite(msg + '\n')
