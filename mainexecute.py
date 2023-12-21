import subprocess
import time
import os
import sys

# process_list = []

# def is_process_running(process_name):
#     #this one to keep tab of the client side and keyboard && mouse, since it might crash
    
#     #specifically also keeping tab of the webserver
#     cmd = 'tasklist /fi "imagename eq {}"'.format(process_name)
#     output = subprocess.check_output(cmd, shell=True).decode()
#     if process_name.lower() in output.lower():
#         return True
#     else:
#         return False


# def if_process_running(pid):
#     """ Check if a process with the given PID is still running. """
#     try:
#         os.kill(pid, 0)
#     except OSError:
#         return False
#     else:
#         return True




# def monitor_server(process):
#     """ Monitor the server process, restart if it stops. """
#     try:
#         while True:
#             if not is_process_running(process.pid):
#                 print("Server crashed, restarting...")
#                 process = start_server()
#             time.sleep(60)  # Check every 60 seconds
#     except KeyboardInterrupt:
#         print("Monitoring stopped.")    
# #also have to make an additional checking method for both client and server side

# # Ctrl+shift+W

# is_process_running("chrome.exe")


def start_server():
    """ Start the server and return the process. """
    command = "python manage.py runserver 0.0.0.0:8000"
    process = subprocess.Popen(command,
                               shell=True,
                               cwd = r"C:\Users\duong\Documents\autostart\virtual-assistant\Store-django")
    return process


def start_screen_control():
    """start the screen control process"""
    command = "python screencontrol.py"
    process = subprocess.Popen(command,
                               shell=True,
                               cwd = r"C:\Users\duong\Documents\autostart")
    return process


start_screen_control()
start_server()