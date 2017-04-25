#coding=utf-8
# 游戏虽然是横屏的,但是坐标系都是按照手机的左上角的作为(0 ,0) 原始坐标系
global personMoveuping
global personMovedowning
global personMovelefting
global personMoverighting

import touch
# 中心 中点(287, 409)  半径 150
centerX = 291
centerY = 409
radius = 200
def left():
    global personMovelefting
    #左边 (262, 259)

    if not personMovelefting:
        personMovelefting = True
        moveMotion(centerX, centerY, centerX, centerY - radius)

def right():
    global personMoverighting
    #   右(287, 559)

    if not personMoverighting:
        personMoverighting = True
        moveMotion(centerX, centerY, centerX, centerY + radius)
def up():
    #   上(437, 409)
    global personMoveuping
    if not personMoveuping:
        personMoveuping = True
        moveMotion(centerX, centerY, centerX + radius, centerY)
def down():
    #   下(137, 409)
    global personMovedowning
    if not personMovedowning:
        personMovedowning = True
        moveMotion(centerX, centerY, centerX - radius, centerY)



# 结束点击
def overTouch():
    print "overTouch"
    touch.endTouch()
    global personMoveuping
    global personMovedowning
    global personMovelefting
    global personMoverighting

    personMoveuping = False
    personMovedowning = False
    personMovelefting = False
    personMoverighting = False

def moveMotion(startX, startY, endX, endY):
    global personMoveuping
    global personMovedowning
    global personMovelefting
    global personMoverighting
    k = 0
    if (startX - endX != 0):
        k = (startY - endY) / (startX - endX)
    b = startY - startX * k;
    touch.startTouch(startX, startY)
    # print "start %d , %d", startX, startY

    for moveX in range(radius):
        if not (personMoveuping | personMovedowning | personMovelefting | personMoverighting):
            print "overTouch break"
            break;
        if (moveX % 50 == 0):

            # print "ismove personMovedowning "+ str(personMovedowning)
            # print "ismove personMoveuping "+ str(personMoveuping)
            # print "ismove personMovelefting "+ str(personMovelefting)
            # print "ismove personMoverighting "+ str(personMoverighting)
            if  personMoveuping :
                touch.moveTouch(startX + moveX, moveX*k + b)
            elif personMovedowning :
                touch.moveTouch(startX - moveX, moveX * k + b)
            elif  personMoverighting:
                touch.moveTouch(startX, startY + moveX)

                # 下面的代码可以斜着走
                # if k == 0:
                #     touch.moveTouch((startY + moveX), startY + moveX)
                # else:
                #     touch.moveTouch((startY + moveX) / k  , startY + moveX)
            elif personMovelefting :
                touch.moveTouch(startX, startY - moveX)
                # if k == 0:
                #     touch.moveTouch((startY + moveX), startY - moveX)
                # else:
                #     touch.moveTouch((startY + moveX) / k  , startY - moveX)

