import os
def main() :

    os.system("adb shell sendevent ")

def startTouch(x, y):

    os.system("adb shell sendevent /dev/input/event4 3 58 62") # ABS_MT_PRESSURE   ===开始
    os.system("adb shell sendevent /dev/input/event4 3 53 " + str(x)) # ABS_MT_POSITION_X
    os.system("adb shell sendevent /dev/input/event4 3 54 "+ str(y)) # ABS_MT_POSITION_Y
    os.system("adb shell sendevent /dev/input/event4 3 57 0") # ABS_MT_TRACKING_ID
    os.system("adb shell sendevent /dev/input/event4 0 2 0") # SYN_MT_REPORT    === 用于同步分离
    os.system("adb shell sendevent /dev/input/event4 1 330 1") # BTN_TOUCH            DOWN

def move(x,y):
    os.system()

if __name__ == '__main__':
    main()