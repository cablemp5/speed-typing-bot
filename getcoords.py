import pyautogui
import time
import winsound


def coords(delay):
    coordlist = [];
    time.sleep(delay)
    winsound.PlaySound("beep",winsound.SND_FILENAME);
    print(pyautogui.position())
    coordlist.append(pyautogui.position().x)
    coordlist.append(pyautogui.position().y)
    time.sleep(delay)
    winsound.PlaySound("beep",winsound.SND_FILENAME);
    print(pyautogui.position())
    coordlist.append(pyautogui.position().x)
    coordlist.append(pyautogui.position().y)
    return coordlist