#!/usr/bin/env python3

import pyautogui, time
from pyautogui import hotkey
time.sleep(5)
f = open("shrek", 'r')
for word in f:
    pyautogui.click(131,223)
    time.sleep(1)
    pyautogui.click(1293,491)
    time.sleep(1)
    pyautogui.typewrite("cyrille")
    time.sleep(1)
    pyautogui.click(1380,530)
    time.sleep(1)
    pyautogui.click(1365,588)
    time.sleep(1)
    pyautogui.typewrite(word)