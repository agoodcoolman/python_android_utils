import os
import android_print

def connect(ip) :
    retuslt = os.popen("adb connect " + ip);
    android_print("adb connect " + ip)
    isConnected = False;
    if "connected" in retuslt.read():
        isConnected = True;

    return isConnected;