import win32gui
import pyautogui
import time

previous_hwnd = 'testname'

def toggle_application_focus(window_title):
    hwnd = win32gui.FindWindowEx(0,0,0, window_title)
    win32gui.SetForegroundWindow(hwnd)



window_title = "testname"
pyautogui.press("alt")
time.sleep(.1)
toggle_application_focus(window_title)