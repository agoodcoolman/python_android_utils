# -*- coding:utf-8 -*-
import os
import sys, getopt
# ips = ["192.168.1.87"]
ips = ["192.168.1.87"]

class Device:
    ip = ""
    isConnected = False

def main():
        sysencodetype = sys.getfilesystemencoding()
        print "脚本名：".decode("utf-8").encode(sysencodetype), sys.argv[0]
        opts, args = getopt.getopt(sys.argv[1:], "hi:h:", ["ip=", "apk="])
        connectip =""
        apkfile = ""
        for op, value in opts:
            if op == "-i":
                connectip = value
            elif op == "--ip":
                connectip = value
            elif op == "--apk":
                apkfile = value
            elif op == "-h":
                print "--apk=指定要安装的apk的文件的地址, --ip=指定要安装的机器的ip地址,前提打开了adb 远程调试工具".decode("utf-8").encode(sysencodetype)
                break
        if connectip:
            print "adb connect ", connectip
            p =  os.popen("adb connect "+ connectip)

            print p.read().decode("utf-8").encode(sysencodetype)
        else:
            # 这里是空的ip地址,那么就直接使用默认的两个ip地址
            ipslength = len(ips)
            devices = []
            for index in range(len(ips)) :
               p = os.popen("adb connect " + ips[index])
               if "connected" in p.read():
                   print ips[index] + "调试连接成功".decode("utf-8").encode(sysencodetype)
                   device = Device()
                   device.ip = ips[index];
                   device.isConnected = True
                   devices.append(device)

               else:
                   print ips[index] + "调试连接失败".decode("utf-8").encode(sysencodetype)

            if apkfile == "":
                print "apk的文件安装路径为空".decode("utf-8").encode(sysencodetype)
            else: # 不为空
                if len(devices):
                    for dev in devices:
                        print "adb -s " + dev.ip + " install -r " + apkfile
                        p = os.popen("adb -s " + dev.ip + " install -r " + apkfile)
                        # print p.read().decode("utf-8").encode(sysencodetype)
                        if "Success" in p.read():
                            print dev.ip + "安装成功".decode("utf-8").encode(sysencodetype)
                            # 安装成功之后启动
                            # os.popen("adb -s " + dev.ip + " reboot shell am start -n com.deao.androidvisitor/com.deao.androidvisitor.regisiter.SecondVistorResgisterActivity")
                            allpackage = os.popen("adb shell ps")
                            # for line in allpackage.readlines():
                            #     if "monkey.android.wifiadb" in line: # wifi adb 调试关闭
                            #         apppid = line.decode("utf-8").encode(sysencodetype).split("   ")[1]
                            #         print ("adb shell kill " + apppid).decode("utf-8").encode(sysencodetype)
                            #         # 关掉adb调试
                            #         os.popen("adb shell kill " + apppid)
                            #         # 启动软件的主界面
                        else:
                            print dev.ip + "安装失败".decode("utf-8").encode(sysencodetype)


if __name__ == '__main__':
    main();

#python install.py --apk=E:\worktemp\ProjectCodeManager\A3fangkeji\AndroidVisitor\AndroidVisitor-release-20170228-v1.13.5-580-550.apk

