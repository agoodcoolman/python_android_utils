#coding=utf-8


import sys
import win32api
from time import sleep
# 下面是相当于自己监控键盘.有个框架,pyhook监控键盘的操作
import win32con
import threading
def main() :
    while True:
        content = raw_input("input:")
        print content

def forenter():
    while True:
        win32api.keybd_event(13, 0, 0, 0)  # enter键位码是13
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        sleep(0.1)

if __name__ == '__main__':
    # thread = threading.Thread(target=forenter())
    # thread.setDaemon(True)
    # thread.start()
    main()