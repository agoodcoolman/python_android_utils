#coding=utf-8
# 游戏虽然是横屏的,但是坐标系都是按照手机的左上角的作为(0 ,0) 原始坐标系

import touch
# 中心 中点(287, 409)  半径 150
centerX = 284
centerY = 438
radius = 200

mouseCenterX = 284
mouseCenterY = 938
def left(id = 0):
    #左边 (262, 259)
        moveMotion(centerX, centerY, centerX,          centerY - radius, id)
def right(id = 0):
    #   右(287, 559)
        moveMotion(centerX, centerY, centerX,          centerY + radius, id)
def up(id = 0):
    #   上(437, 409)
        moveMotion(centerX, centerY, centerX + radius, centerY, id)
def down(id = 0):
    #   下(137, 409)
        moveMotion(centerX, centerY, centerX - radius, centerY, id)

def upRight(id = 0):
        moveMotion(centerX, centerY, (centerX + radius + centerX)/2, (centerY + radius +centerY)/2, id)
def upLeft(id = 0):
        moveMotion(centerX, centerY, (centerX + radius + centerX)/2,  (centerY - radius + centerY)/2, id)
def downLeft(id = 0):
        moveMotion(centerX, centerY, (centerX - radius + centerX)/2, (centerY + centerY - radius)/2, id)
def downRight(id = 0):
        moveMotion(centerX, centerY, (centerX - radius + centerX)/2, (centerY + centerY + radius)/2, id)


def mouseleft(id = 0):
    #左边 (262, 259)
        moveMotion(mouseCenterX, mouseCenterY, mouseCenterX,          mouseCenterY - radius, id)
def mouseright(id = 0):
    #   右(287, 559)
        moveMotion(mouseCenterX, mouseCenterY, mouseCenterX,          mouseCenterY + radius,  id)
def mouseup(id = 0):
    #   上(437, 409)
        moveMotion(mouseCenterX, mouseCenterY, mouseCenterX + radius, mouseCenterY, id)
def mousedown(id = 0):
    #   下(137, 409)
        moveMotion(mouseCenterX, mouseCenterY, mouseCenterX - radius, mouseCenterY, id)

def mouseupRight(id = 0):
        moveMotion(mouseCenterX, mouseCenterY, (mouseCenterX + radius + mouseCenterX)/2, (mouseCenterY + radius +mouseCenterY)/2, id)
def mouseupLeft(id = 0):
        moveMotion(mouseCenterX, mouseCenterY, (mouseCenterX + radius + mouseCenterX)/2,  (mouseCenterY - radius + mouseCenterY)/2, id)
def mousedownLeft(id = 0):
        moveMotion(mouseCenterX, mouseCenterY, (mouseCenterX - radius + mouseCenterX)/2, (mouseCenterY + mouseCenterY - radius)/2, id)
def mousedownRight(id = 0):
        moveMotion(mouseCenterX, mouseCenterY, (mouseCenterX - radius + mouseCenterX)/2, (mouseCenterY + mouseCenterY + radius)/2, id)



# 结束点击
def overTouch():
    print "overTouch"
    touch.endTouch()


def moveMotion(startX, startY, endX, endY, id = 0):
    print "moving start", startX, startY, endX, endY
    touch.startTouch(startX, startY)
    moveXpostion = 0;
    moveYpostion = 0;

    for moveX in range(6):
        moveXpostion = moveX * 20 + startX;
        # 判断是否在取值范围内
        # 垂直X轴
        if (startX - endX) == 0:
            moveXpostion  = startX
            if startY > endY:
                moveYpostion = startY - moveX * 20;
            else:
                moveYpostion = moveX * 20 + startY;

        # 垂直Y轴
        elif (startY - endY == 0):
            if startX > endX:
                moveXpostion = startX - moveX * 20
            else:
                moveXpostion = startX + moveX * 20
            moveYpostion = startY;
        else:
            moveXpostion = startX + moveX * 20
            moveYpostion = ((moveXpostion - startX) / (endX - startX))(endY - startY) + startY
        touch.moveTouch(moveXpostion, moveYpostion, id)
        print "moving", moveXpostion, moveYpostion

