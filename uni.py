# -*- coding:utf-8 -*-
#卸载软件
import sys, getopt, os
# ips = ["192.168.1.7"]
ips = ["192.168.1.7", "192.168.1.87"]
# 卸载 设备上的访客机软件
def main() :
    sysencodetype = sys.getfilesystemencoding()
    print "脚本名：".decode("utf-8").encode(sysencodetype)
    for ip in ips:
        result = os.popen("adb connect " + ip)
        if "connected" in result.read():
            print (ip + "测试连接成功").decode("utf-8").encode(sysencodetype)
            re = os.popen("adb -s " + ip + " uninstall com.deao.androidvisitor")
            print ("adb -s " + ip + " uninstall com.deao.androidvisitor").decode("utf-8").encode(sysencodetype)
            if "Success" in re.read():
                print (ip + ", 访客机程序卸载成功").decode("utf-8").encode(sysencodetype)


if __name__ == '__main__':
        main()