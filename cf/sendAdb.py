# coding=utf-8
#把所有的指令都封装成数据
import os
#lines 把所有的操作的命令直接封装 发送到这里
def sendAdbmotion(lines):
    for line in lines:
        os.system(line)

# 这里把要进行的所有的操作进行合并
# 只封装两个点的触控
# 前面一个是触摸的移动 ,可能两个点同时移动
# 后面一个是点击点
# 按照 x,y 两个位置是一个点的方式存储
def resolveMontion(touchposotion = [], clickpostion = []):
    if len(clickpostion) == 0: # 没有点击
        if len(touchposotion) == 0: # 没有触摸移动
            print "不执行操作"
        elif len(touchposotion) == 2: # 一个移动触摸点
            print "执行1个触摸操作"
        elif len(touchposotion) == 4: # 两个移动触摸点
            print "执行2个触摸操作"
    elif len(clickpostion) == 2: # 有点击
        if len(touchposotion) == 0:  # 没有触摸移动
            print "执行1个点击操作"
        elif len(touchposotion) == 2:  # 一个移动触摸点
            print "执行1个点击1个触摸操作"
        elif len(touchposotion) == 4:  # 两个移动触摸点
            print "暂时不考虑这个"

