import pyautogui
import time
time.sleep(4)
count = 0
while count<10:
    pyautogui.typewrite("mairu")
    pyautogui.press("enter")
    count =count+1

