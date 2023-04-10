import numpy as np
import pyautogui as gui
import keyboard as key


def click_to_start(x = 44, y = 144):
    gui.moveTo(x, y)
    gui.click(button='left')
