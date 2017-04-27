#coding=utf-8
# 主要用来写 点击触摸事件的逻辑
# 这里改造成,键盘/鼠标 事件 这里这里进行统一汇聚.并且转换成手机上游戏的事件
import math
import touch
import PhoneMontionEngine
from MontionPool import Montion
# 移动中心 中点  半径
centerX = 284
centerY = 438
radius = 200

mouseCenterX = 284
mouseCenterY = 938


# 游戏的操作类型  人移动, 视角方向, 点击
MontionType = ["personMoving", "perspective", "click"]



def mouseMoving(movingAngle):

    montion_zuzhuang = Montion("perspective", [mouseCenterX, mouseCenterY], movingAngle)

    # PhoneMontionEngine.runMotion(montion_zuzhuang)

def up():
    montion_zuzhuang = Montion("personMoving", [centerX, centerY], math.pi/2)
    PhoneMontionEngine.runMotion(montion_zuzhuang)

def down():
    montion_zuzhuang = Montion("personMoving", [centerX, centerY], 3*math.pi/2)
    PhoneMontionEngine.runMotion(montion_zuzhuang)

def left():
    montion_zuzhuang = Montion("personMoving", [centerX, centerY], math.pi)
    PhoneMontionEngine.runMotion(montion_zuzhuang)

def right():
    montion_zuzhuang = Montion("personMoving", [centerX, centerY], 0)
    PhoneMontionEngine.runMotion(montion_zuzhuang)

def overPeronMovingTouch():
    # 人在移动的时候,取消人的移动了
    print "这里是方向键,结束或者是什么结束"
    PhoneMontionEngine.removeMontion("personMoving")

def overMouseTouch():
    # print "鼠标的移动结束"
    PhoneMontionEngine.removeMontion("perspective")

def squat():
    montion = Montion("click", [64, 71])
    PhoneMontionEngine.runMotion(montion)

def jump():
    montion = Montion("click", [473, 1871])
    PhoneMontionEngine.runMotion(montion)

def changeGun():
    montion = Montion("click", [64, 1497])
    PhoneMontionEngine.runMotion(montion)

def overClick():
    PhoneMontionEngine.removeMontion("click")

def startEngine():
    PhoneMontionEngine.startEngine()

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
    os.system("adb -s " + touch.device + " shell sendevent " + touch.eventfile + " 3 57 " + str(id))  # ABS_MT_TRACKING_ID 同时点击,同时触摸,这里要设置为1,相当于多点触控中的点2
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT    ===
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 2 0")  # SYN_MT_REPORT
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 1 330 0")  # BTN_TOUCH
    os.system("adb -s " + touch.device + " shell sendevent  " + touch.eventfile + " 0 0 0")  # SYN_REPORT