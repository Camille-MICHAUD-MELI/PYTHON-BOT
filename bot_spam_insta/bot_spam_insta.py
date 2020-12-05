
#!/usr/bin/env python3

import pyautogui, time
time.sleep(5)
f = open("shrek", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")