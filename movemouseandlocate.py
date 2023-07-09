import win32gui,win32con,win32com.client
import pyautogui
import time

import win32gui
import win32con

def windowEnumHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def bringToFront(window_name):
    top_windows = []
    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        # print(i[1])
        if window_name.lower() in i[1].lower():
            # print("found", window_name)
            win32gui.ShowWindow(i[0], win32con.SW_SHOWMAXIMIZED)
            win32gui.SetForegroundWindow(i[0])
            break

# Test with notepad
if __name__ == "__main__":
    winname = "chrome"
    bringToFront(winname)



# previous_hwnd = 'testname'

# def toggle_application_focus(window_title):

#     hwnd = win32gui.FindWindowEx(0,0,0, window_title)
#     win32gui.SetForegroundWindow(hwnd)

# def get_fore_ground():
#     time.sleep(2)
#     Minimize = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)


# window_title = "testname"
# pyautogui.hotkey("ctrl", "c")

# time.sleep(.1)
# toggle_application_focus(window_title)
# get_fore_ground()