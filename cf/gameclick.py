#coding=utf-8
#android点击脚本
import os
import touch
import gametouch
def click(x,y, id = 0):

        os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 58 62")  # ABS_MT_PRESSURE   ===
        os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 53 " + str(x))  # ABS_MT_POSITION_X
        os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 54 " + str(y))  # ABS_MT_POSITION_Y
        os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 57 " + str(id))  # ABS_MT_TRACKING_ID 同时点击,同时触摸,这里要设置为1,相当于多点触控中的点2
        os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT    ===


def onlyClick(x,y):
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 58 67")
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 53 " + str(x))
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 54 " + str(y))
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 3 57 1") # 这里是id
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 1 330 1")
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 0 0")
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 1 330 0")
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 0 0")


















