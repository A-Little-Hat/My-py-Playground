import time
import pyautogui

time.sleep(10)
word = "enter your text"

for i in range(1, 100):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
