# -*- coding:utf-8 -*-
import os
import android_print

def getDevice(ip) :
    popen = os.popen("adb -s " + ip + " shell cat /system/build.prop | grep \"product\"")
    readline = popen.readline()
    android_print.printinfo( popen)
    if readline.startswith("ro.product.model="):
        # 设备型号
        devicemodel = readline.split("=")[1]
        return devicemodel
# width * heigh
def getDeviceSize(ip):
    popen = os.popen(" adb -s "+ ip +" shell dumpsys window | grep init=")
    readlines = popen.readlines()
    for line in readlines:
        android_print.printinfo(line)
        if "init=" in line:
            print line.split("=")[1].split(" ")
            return line.split("=")[1].split(" ")[0]
    return  ""


if __name__ == '__main__':
    print getDeviceSize("192.168.1.87");