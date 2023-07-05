import win32gui,win32con
import pyautogui
import time

previous_hwnd = 'testname'

def toggle_application_focus(window_title):
    hwnd = win32gui.FindWindowEx(0,0,0, window_title)
    win32gui.SetForegroundWindow(hwnd)

def get_fore_ground():
    time.sleep(2)
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

window_title = "testname"
pyautogui.press("alt")
time.sleep(.1)
toggle_application_focus(window_title)
get_fore_ground()