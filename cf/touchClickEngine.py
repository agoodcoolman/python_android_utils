#coding=utf-8
# 主要用来写 点击触摸事件的逻辑
#
from cf import gameclick
import touch
motioncount = 0;
import gametouch
def touchMontion       (x, y):
    print ""

def click(x, y):
    print ""

def up():
    gametouch.up()

def down():
    gametouch.down()

def left():
    gametouch.left()

def right():
    gametouch.right()
    print ""

def overTouch():
    gametouch.overTouch()

def squat():
    gameclick.click(64, 71)


def jump():
    test()
    # gameclick.click(473, 1871)

def changeGun():
    gameclick.click(64, 1497)
def overClick():
    print ""

def test():
    import os
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 58 62")  # ABS_MT_PRESSURE   ===
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 53 " + str(284))  # ABS_MT_POSITION_X
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 54 " + str(438))  # ABS_MT_POSITION_Y
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 57 0")  # ABS_MT_TRACKING_ID
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT    ===
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 1 330 1")  # BTN_TOUCH            DOWN
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 58 1")  # ABS_MT_PRESSURE   ===
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 53 " + str(287))  # ABS_MT_POSITION_X
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 54 " + str(559))  # ABS_MT_POSITION_Y
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 57 " + str(id))  # ABS_MT_TRACKING_ID
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT    ===

    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 58 62")  # ABS_MT_PRESSURE   ===
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 53 " + str(473))  # ABS_MT_POSITION_X
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 54 " + str(1871))  # ABS_MT_POSITION_Y
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 57 " + str(
        id))  # ABS_MT_TRACKING_ID 同时点击,同时触摸,这里要设置为1,相当于多点触控中的点2
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT    ===
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 1 330 0")  # BTN_TOUCH
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 0 0")  # SYN_REPORT