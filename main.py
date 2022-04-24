import getcoords

import keyboard
from pynput.keyboard import Key, Controller
import time
import pyautogui
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
board = Controller()

times_pressed = 0
top_left = [0,0]
bottom_right = [0,0]

time.sleep(3)

#img = pyautogui.screenshot(region=(top_left[0],top_left[1],bottom_right[0]-top_left[0],bottom_right[1]-top_left[1]))
img = pyautogui.screenshot(region=(234,534,1000,300))

img.show()

output = pytesseract.image_to_string(img)

output = output.replace("\nchange display format","")
output = output.replace("|","I")
output = output.replace("{","")

output = " ".join(output.split())

print(output)

for word in output.split(" "):
    board.type(word + " ")
    time.sleep(0.3)








