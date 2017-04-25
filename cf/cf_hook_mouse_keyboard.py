#coding=utf-8
# 这里监控 鼠标事件/键盘事件
import pyHook
import thread

import click
import gametouch
import pythoncom
import touch
import threading
def onMouseEvent(event):
    "处理鼠标事件"
    # fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
    # fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    # fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    # fobj.writelines("Message:%d\n" % event.Message)
    # fobj.writelines("Time_sec:%d\n" % event.Time)
    # fobj.writelines("Window:%s\n" % str(event.Window))
    # fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    # fobj.writelines("Position:%s\n" % str(event.Position))
    # fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
    return True


def onKeyboardEventDown(event):
    "处理键盘事件"

    if str(event.Key) == "Lcontrol": # 左边control
        click.click(64, 71)
    elif str(event.Key) == "Space": # 空格
        click.click(473, 1871)
    elif str(event.Key) == "Q":
        click.click(64, 1497)
    elif str(event.Key) == "W":
        gametouch.up()
    elif str(event.Key) == "A":
        gametouch.left()
    elif str(event.Key) == "S":
        gametouch.down()
    elif str(event.Key) == "D":
        gametouch.right()
    return True

def onKeyboardEventUP(event):

    if str(event.Key) == "W":
        gametouch.overTouch()
    elif str(event.Key) == "A":
        gametouch.overTouch()
    elif str(event.Key) == "S":
        gametouch.overTouch()
    elif str(event.Key) == "D":
        gametouch.overTouch()
    return True

def startMotion():

    touch.device = "DU2TAN14A8019404"
    # touch.device = "192.168.1.32"
    touch.eventfile = "/dev/input/event4"
    gametouch.personMoveuping = False
    gametouch.personMovedowning = False
    gametouch.personMovelefting = False
    gametouch.personMoverighting = False

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
    pythoncom.PumpMessages()


if __name__ == '__main__':
    threading_thread = threading.Thread(target=startMotion())
    threading_thread.setDaemon(True)
    threading_thread.start()