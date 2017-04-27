#coding=utf-8
# 这里统一把从 鼠标/键盘引擎中 封装的动作的数据都在这里进行统一的逻辑封装
# 这里是把游戏中的动作,解析成adb里面个的event的事件
import threading
import Mouse_keybord_Engine
import math
import sendAdb
from stack import Queue
# 触摸事件往外的跨度,越大越快
radiusIncreaseSpan = 50
# 线程锁
mutex = threading.Lock()
# 控制执行到手机上操作的线程的开关
runningMontionswitch = False

# 最后封装的可以直接运行的动作了
# 只考虑多点触控中的两个点,所以这里情况如下:
# 1.只有一个点击
# 2.只有一个触摸
# 3.一个点击,一个触摸
# 4.两个触摸
runningFinalMotion = Queue(2)

# 这个方法就对进来的所有的操作进行处理,
# 比如两个方向键要处理
# 比如进来视角的方向,要判断是否有点击,是否有其它的人移动的操作
# 要把所有的数据操作成最后执行的 触摸/点击  合集
# 把要进行的操作 整合成最后的操作
def runMotion(Montion):
    if mutex.acquire(): # 对变量加同步锁
        if str(Montion.montionType).lower() == "perspective":  # 看的视角
            find_montion = runningFinalMotion.findMontion("personMoving")
            if not find_montion:
                runningFinalMotion.enqueue(Montion)
            else:
                find_montion.postion = Montion.position
                find_montion.angle = Montion.angle

        elif str(Montion.montionType).lower() == "personMoving":  # 人移动
            # 人移动的话,asdw四个键的操作.这里可以直接把数据给处理了.两个键
            # 同时按下去的,那么我就把角度相加 取平均值(正常情况)
            montion = runningFinalMotion.findMontion("personMoving")
            if not montion:
                montion.angle = (Montion.angle + montion.angle)/ 2
        elif str(Montion.montionType).lower() == "click":  # 点击
            runningFinalMotion.enqueue(Montion)

        mutex.release()

# 动作执行完毕,要结束了
# 把动作从执行的参数中移除
def removeMontion(montionname):
    if mutex.acquire():  # 对变量加同步锁
        runningFinalMotion.remove(montionname)

        mutex.release()


# 循环运行所有的操作
def runAllMontion():
    touch = []
    click = []
    while (runningMontionswitch):
        if mutex.acquire():
            if not runningFinalMotion.isempty():
                if runningFinalMotion.size == 1: # 单点
                   if  runningFinalMotion.findMontion("click"): # 点击
                       click = runningFinalMotion[0].position;
                   else: #不是点击
                       centosposition = runningFinalMotion[0].position
                       radiu = runningFinalMotion[0].currentRadiu
                       radiu += radiusIncreaseSpan # 限制触摸的范围在一个半径里面.
                       if (radiu> Mouse_keybord_Engine.radius):
                           radiu = Mouse_keybord_Engine.radius
                       angle = runningFinalMotion[0].angle
                       touch.append(centosposition[0] + math.cos(angle) * runningFinalMotion[0].currentRadiu)
                       touch.append(centosposition[0] - math.sin(angle) * runningFinalMotion[0].currentRadiu) # 手机的坐标系的y轴,跟平常的坐标系的y轴是反向

                elif  runningFinalMotion.size == 2:
                    # 不存在两个点击.
                    # 1.一个点击,一个触摸
                    # 2.两个触摸
                    for finalMontion in runningFinalMotion:
                        if finalMontion.montionType == "click": # 1.一个点击,一个触摸
                            click = finalMontion.position
                        else: #2.两个触摸
                            touch = finalMontion.position

                sendAdb.resolveMontion(touch, click)
            mutex.release()



def startEngine():
    global runningMontionswitch
    runningMontionswitch = True;
    thread = threading.Thread(target=runAllMontion)
    thread.setDaemon(True)
    thread.run()


