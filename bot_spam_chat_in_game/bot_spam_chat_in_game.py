#!/usr/bin/env python3

import pyautogui, time, keyboard
time.sleep(5)
f = open("shrek", 'r')
for word in f:
    pyautogui.press("enter")
    pyautogui.typewrite(word)
    pyautogui.press("enter")