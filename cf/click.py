#coding=utf-8
#android点击脚本
import os
import touch
def click(x,y):

    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 3 58 67")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 3 53 " + str(x))
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 3 54 " + str(y))
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 3 57 0")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 0 2 0")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 1 330 1")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 0 0 0")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 0 2 0")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 1 330 0")
    os.system("adb -s "+ touch.device +" shell sendevent  "+ touch.eventfile +" 0 0 0")



















