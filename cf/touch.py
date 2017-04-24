
import os
def main() :

    os.system("adb shell sendevent ")

def startTouch(x, y):

    os.system("adb shell sendevent /dev/input/event4 3 58 62") # ABS_MT_PRESSURE   ===
    os.system("adb shell sendevent /dev/input/event4 3 53 " + str(x)) # ABS_MT_POSITION_X
    os.system("adb shell sendevent /dev/input/event4 3 54 "+ str(y)) # ABS_MT_POSITION_Y
    os.system("adb shell sendevent /dev/input/event4 3 57 0") # ABS_MT_TRACKING_ID
    os.system("adb shell sendevent /dev/input/event4 0 2 0") # SYN_MT_REPORT    ===
    os.system("adb shell sendevent /dev/input/event4 1 330 1") # BTN_TOUCH            DOWN

def moveTouch(x,y):

    os.system("adb shell sendevent /dev/input/event4 3 58 40")  # ABS_MT_PRESSURE   ===
    os.system("adb shell sendevent /dev/input/event4 3 53 " + str(x))  # ABS_MT_POSITION_X
    os.system("adb shell sendevent /dev/input/event4 3 54 " + str(y))  # ABS_MT_POSITION_Y
    os.system("adb shell sendevent /dev/input/event4 3 57 0")  # ABS_MT_TRACKING_ID
    os.system("adb shell sendevent /dev/input/event4 0 2 0")  # SYN_MT_REPORT    ===
    os.system("adb shell sendevent /dev/input/event4 0 0 0")  # BTN_TOUCH            DOWN


def endTouch():
    os.system("adb shell sendevent /dev/input/event4 0 2 0") # SYN_MT_REPORT
    os.system("adb shell sendevent /dev/input/event4 1 330 0") # BTN_TOUCH
    os.system("adb shell sendevent /dev/input/event4 0 0 0") #SYN_REPORT


if __name__ == '__main__':
    main()