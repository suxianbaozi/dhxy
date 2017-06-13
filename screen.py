from ctypes import *
from ctypes.wintypes import *
import time
HWND_BROADCAST = 0xffff
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MonitorPowerOff = 2
SW_SHOW = 5

def closeScreen():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MonitorPowerOff)

def openSecreen():
    windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)



# shell32 = windll.LoadLibrary("shell32.dll")
# shell32.ShellExecuteW(None,'open', 'rundll32.exe', 'USER32,LockWorkStation','',SW_SHOW)

if __name__ == "__main__":

    while True:
        closeScreen()
        time.sleep(15*60)
        openSecreen()
        time.sleep(20)
