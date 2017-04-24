# -*- coding:utf-8 -*-
import os
import android_print

def androidclick( deviceid, localtion = [0, 0]) :
    android_print("adb -s " + deviceid + " shell input click " + localtion[0] + " " +  localtion[1])
    result = os.popen("adb -s " + deviceid + " shell input click " + localtion[0] + " " +  localtion[1])
