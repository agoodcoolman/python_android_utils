#coding=utf-8

# 封装的是到手机上的操作
class Montion(object):
    # 手机上要执行的操作都放到这个里面
    montionType =  ""
    # 代表初始化的位置,点击就是点击位置,如果是触摸就是触摸滑动的中心点
    position = []
    angle = 0 # 角度,方向角度
    # 当前的半径,这个半径会增大
    currentRadiu = 0

    def __init__(self, montionType, position, angle = 0):
        self.montionType = montionType;
        self.position = position;
        self.angle = angle;




