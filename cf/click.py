import os

#android click event
# position x
# position y
def click(x, y):

    os.system("adb shell sendevent /dev/input/event4 3 58 64")
    os.system("adb shell sendevent /dev/input/event4 3 53 " + str(x))
    os.system("adb shell sendevent /dev/input/event4 3 54 " + str(y))
    os.system("adb shell sendevent /dev/input/event4 3 57 0")
    os.system("adb shell sendevent /dev/input/event4 0 2 0")
    os.system("adb shell sendevent /dev/input/event4 1 330 1")
    os.system("adb shell sendevent /dev/input/event4 0 0 0")
    os.system("adb shell sendevent /dev/input/event4 0 2 0")
    os.system("adb shell sendevent /dev/input/event4 1 330 0")