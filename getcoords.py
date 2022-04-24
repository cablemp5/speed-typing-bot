import pyautogui
import time

def coords(delay):
    time.sleep(delay)
    print(pyautogui.position())