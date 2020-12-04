#!/usr/bin/env python3 
""" to be read by your computer you nedd this line in the header """


import pyautogui, time
""" import the required module """
time.sleep(5)
""" let you the time to go on the page where you want to spam your text """
f = open("shrek", 'r')
""" open the document which contain the text to be displayed """
for word in f:
    """ say that every time he will see some word he will do this """
    pyautogui.typewrite(word)
    pyautogui.press("enter")