#coding=utf-8
# 这里监控 鼠标事件/键盘事件
import pyHook
import thread

import time

import gameclick
import gametouch
import pythoncom
import touch
import threading
import Mouse_keybord_Engine
import math

# 代表鼠标的灵敏度是多少
sensitivity = 20;
timesensitivity = 100
prePosition = [0, 0]
preTime = 0;
preatan = 0;
def onMouseEvent(event):
    global prePosition
    global preTime
    global preatan
    #"处理鼠标事件"
    # 判断鼠标的移动方向
    currentposition = event.Position
    # 已经两点,求 坐标系
    atan = math.pi/2; # 默认90°
    if (currentposition[0] - prePosition[0]) != 0:
        if currentposition[1] - prePosition[1]!= 0 :
            atan = math.atan(-(currentposition[1] - prePosition[1]) / (currentposition[0] - prePosition[0]))
        else:
            if currentposition[0] - prePosition[0] > 0 :
                atan = 0
            else:
                atan = math.pi
    else: # currentposition[0] - prePosition[0] = 0 这里是等于0
        if currentposition[1] - prePosition[1] > 0:
            atan = 3 * math.pi / 2
        else:
            atan = math.pi /2

    if preTime == 0:
        preTime = event.Time;


    if (abs(prePosition[0] - currentposition[0]) > sensitivity or abs(prePosition[1] - currentposition[1]) > sensitivity) and (event.Time - preTime > timesensitivity) and (preatan != atan):
        preTime = event.Time
        print atan
        prePosition = currentposition
        preTime = atan
        Mouse_keybord_Engine.mouseMoving(atan)
    else:
        Mouse_keybord_Engine.overMouseTouch()

    return True



def onKeyboardEventDown(event):
    "处理键盘事件"
    if str(event.Key) == "Lcontrol":  # 左边control
        Mouse_keybord_Engine.squat()
    elif str(event.Key) == "Space":  # 空格
        Mouse_keybord_Engine.jump()
    elif str(event.Key) == "Q":
        Mouse_keybord_Engine.changeGun()
    elif str(event.Key) == "W":
        Mouse_keybord_Engine.up()
    elif str(event.Key) == "A":
        Mouse_keybord_Engine.left()
    elif str(event.Key) == "S":
        Mouse_keybord_Engine.down()
    elif str(event.Key) == "D":
        Mouse_keybord_Engine.right()

    return True

def onKeyboardEventUP(event):

    if str(event.Key) == "W":
        Mouse_keybord_Engine.overPeronMovingTouch()
    elif str(event.Key) == "A":
        Mouse_keybord_Engine.overPeronMovingTouch()
    elif str(event.Key) == "S":
        Mouse_keybord_Engine.overPeronMovingTouch()
    elif str(event.Key) == "D":
        Mouse_keybord_Engine.overPeronMovingTouch()
    return True

def startMotion():

    touch.device = "DU2TAN14A8019404"
    # touch.device = "192.168.1.32"
    touch.eventfile = "/dev/input/event4"
    # gametouch.personMoveuping = False
    # gametouch.personMovedowning = False
    # gametouch.personMovelefting = False
    # gametouch.personMoverighting = False
    # Mouse_keybord_Engine.startEngine()
    # 创建hook句柄
    hm = pyHook.HookManager()

    # 监控键盘
    hm.KeyDown = onKeyboardEventDown
    hm.KeyUp = onKeyboardEventUP
    hm.HookKeyboard()

    # 监控鼠标
    hm.MouseAll = onMouseEvent

    hm.HookMouse()

    # 循环获取消息
    pythoncom.PumpMessages(2)


if __name__ == '__main__':
    threading_thread = threading.Thread(target=startMotion())
    threading_thread.setDaemon(True)
    threading_thread.start()