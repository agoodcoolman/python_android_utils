# -*- coding:utf-8 -*-

import sys, getopt, os
ips = ["192.168.1.7", "192.168.1.87"]
# 卸载 设备上的访客机软件
def main() :
    sysencodetype = sys.getfilesystemencoding()
    print "脚本名：".decode("utf-8").encode(sysencodetype)
    for ip in ips:
        result = os.popen("adb connect " + ip)
        if "connected" in result.read():
            print (ip + "测试连接成功").decode("utf-8").encode(sysencodetype)
        else:
            print (ip + "测试连接失败").decode("utf-8").encode(sysencodetype)