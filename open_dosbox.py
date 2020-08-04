import time
import os

import pyautogui

def open_dosbox(dosbox_path, filepath, dos_dir_path):
    output_relative_path = filepath.split(dos_dir_path)[1]
    split_char = output_relative_path[0]
    output_relative_path_list = output_relative_path.split(split_char)
    output_dir_path = (split_char.join(output_relative_path_list[0:len(output_relative_path_list) - 1]))[1:]
    filename = output_relative_path_list[len(output_relative_path_list) - 1]
    
    os.system('start "" "' + dosbox_path + '"')
    time.sleep(5)
    pyautogui.press("escape")
    time.sleep(2)

    if len(output_relative_path_list) > 2:
        pyautogui.typewrite("cd " + output_dir_path, interval=0.25)
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("escape")
        time.sleep(2)
        pyautogui.typewrite("T602 " + filename, interval=0.25)
        time.sleep(2)
        pyautogui.press("enter")
    else:
        pyautogui.typewrite("T602 " + filename, interval=0.25)
        time.sleep(2)
        pyautogui.press("enter")
    