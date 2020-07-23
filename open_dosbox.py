import time
import os

import pyautogui

def open_dosbox(dosbox_path, filename):
    document_string = "{0}.602".format(filename)

    os.system('start "" "' + dosbox_path + '"')
    time.sleep(5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("backspace", presses=3)
    time.sleep(2)
    pyautogui.typewrite(document_string)
    time.sleep(2)
    pyautogui.press("enter")