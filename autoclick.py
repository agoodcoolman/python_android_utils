# -*- coding:utf-8 -*-
import os
import sys
# ips = ["192.168.1.87"]
import time
ips = ["192.168.1.87"]
import android_device
import multiprocessing
def adblocat(ip) :

    file = "C:\Users\Administrator\Desktop\\tps-550\\a\\20170328log\\"+ str(time.time())+".txt"

    exists = os.path.exists(file)
    if exists:
        os.mkdir(file)
    # f = open(file, "a")
    # a = os.subprocess.Popen()("adb -s  " + ip + " logcat -v time > " + file)
    popen = os.popen("adb -s  192.168.1.87 logcat -v time > " + file )
    os.system("adb -s "+  ip +" logcat -v time > " + file )



def main():
    sysencodetype = sys.getfilesystemencoding()
    print "脚本名：".decode("utf-8").encode(sysencodetype)

    for ip in ips:
        result = os.popen("adb connect " + ip)
        if "connected" in result.read():
            #  mUnrestrictedScreen=(0,0) 768x1024
            device = android_device.getDevice(ip)
            process = multiprocessing.Process(target=adblocat, args=(ip,))
            process.start()
            if "TPS580" in device:
                for a in range(400):
                    time.sleep(2)
                    # 这里是进入拍照
                    result = os.popen("adb -s " + ip + " shell input tap 247 921")
                    # 延时操作
                    # 点击拍照

            # result = os.popen("adb -s " + ip + " shell input tap 600 890")
            elif "TPS550" in device:
                for a in range(400):
                    time.sleep(3)
                    # 这里是进入拍照
                    # result = os.popen("adb -s " + ip + " shell input tap 619 110")
                    # 550 点击登记
                    result = os.popen("adb -s " + ip + " shell input tap 632 276pip")
                    # 延时操作
                    # time.sleep(3)
                    #点击拍照
                    # result = os.popen("adb -s " + ip + " shell input tap 754 358")

if __name__ == '__main__':
    main();