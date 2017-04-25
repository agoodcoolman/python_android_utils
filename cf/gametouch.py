#coding=utf-8
# 游戏虽然是横屏的,但是坐标系都是按照手机的左上角的作为(0 ,0) 原始坐标系
global uping
global downing
global lefting
global righting

import touch
# 中心 中点(287, 409)  半径 150
def left():
    global lefting
    #左边 (262, 259)

    if not lefting:
        lefting = True
        moveMotion(287, 409, 262, 259)

def right():
    global righting
    #   右(287, 559)

    if not righting:
        righting = True
        moveMotion(287, 409, 287, 287)
def up():
    #   上(437, 409)
    global uping
    if not uping:
        uping = True
        moveMotion(287, 409, 437, 409)
def down():
    #   下(137, 409)
    global downing
    if not downing:
        downing = True
        moveMotion(287, 409, 137, 409)


# 结束点击
def overTouch():
    print "overTouch"
    touch.endTouch()
    global uping
    global downing
    global lefting
    global righting
    # print downing
    # print  uping
    # print  lefting
    # print  righting
    uping = False
    downing = False
    lefting = False
    righting = False

def moveMotion(startX, startY, endX, endY):
    global uping
    global downing
    global lefting
    global righting
    k = 0
    if (startX - endX != 0):
        k = (startY - endY)/ (startX - endX)
    b = startY - startX*k;
    touch.startTouch(startX, startY)
    for moveX in range(endX - startX):
        if (moveX % 20 == 0):
            print downing
            print  uping
            print  lefting
            print  righting
            if downing | uping | lefting | righting:
                touch.moveTouch(moveX, moveX*k + b)
            else:
                break;