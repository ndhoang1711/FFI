import re
import pandas as pd

def listToString(s):
    str1 = "" 
     
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

def CROSS_INT(interfaces, check):
    CROSS = []
    if check == 1:
        for i in interfaces:
            if ("CROSS-VRF Data") not in i:
                CROSS.append("none")
            if ("CROSS-VRF Data") in i:
                cr = i.split("\n")
                for m in cr:
                    if ("CROSS-VRF Data") in m:
                        cross = re.findall("^[^ .]*", m)
                        CROSS.append(cross)

        #CROSS.pop(0)
    else:
         CROSS.append("") 
    CROSS.pop(0)
    return CROSS

def DEVICE_NAME(interfaces, check):
    DNAME = []
    if check == 1:
        for i in interfaces:
            if ("descriptions") in i:
                dn = i.split("\n")
                for m in dn:
                    if ("descriptions") in m:
                        dname = re.findall("[^@+>]+", m)
                        DNAME.append(dname[1])
                        # print(dname[1])
            if ("descriptions") not in i:
                dn = i.split("\n")
                for m in dn:
                    if ("failed") in m:
                        dname = re.findall("(\S+)", m)
                        DNAME.append(dname[0])
        #DNAME.pop(0)
    else:
        DNAME.append("")
    return DNAME


def LAN_INT(interfaces, check):
    LAN = []
    inter = []
    if check == 1:
        for i in interfaces:
            if ("*** Customer LAN ***") in i:
                lan_int = i.split("\n")
                for m in lan_int:
                    if ("*** Customer LAN ***") in m:
                        lan =  listToString(re.findall("^[^ .]*", m)) 
                        inter.append(lan)                        #print(type(lan))
                LAN.append(inter)
                inter = []
            if ("*** Customer LAN ***") not in i:
                LAN.append("none")
        #LAN.pop(0)
    else:
        LAN.append("")
    LAN.pop(0)
    return LAN

# Serial and model device
def MODEL_DEVICE(interfaces, check):
    
    MODEL = []
    if check == 1:
        for i in interfaces:
            if ("Chassis") in i:
                chassis = i.split("\n")
                for m in chassis:
                    if ("Chassis") in m:
                        sn = re.findall("(\S+)", m)
                        if ("chassis") not in sn[2]:
                            MODEL.append(sn[2])
            if ("Chassis") not in i:
                MODEL.append("none")
        #MODEL.pop(0)
    else:
        MODEL.append("")
    MODEL.pop(0)
    return MODEL
    
def SERIAL_DEVICE(interfaces, check):
    SERIAL = []
    if check == 1:
        for i in interfaces:
            if ("Chassis") in i:
                chassis = i.split("\n")
                for m in chassis:
                    if ("Chassis") in m:
                        sn = re.findall("(\S+)", m)
                        if ("show") not in sn[1]:
                            SERIAL.append(sn[1])
            if ("Chassis") not in i:
                SERIAL.append("none")
    else:
        SERIAL.append("")
    SERIAL.pop(0)
    return SERIAL

def WAN_INT(interfaces, check):
    WAN = []
    if check == 1:
        for i in interfaces:
            if ("WAN-VRF Data;") in i:
                wan_int = i.split("\n")
                for m in wan_int:
                    if ("WAN-VRF Data;") in m:
                        wan = re.findall("^[^ .]*", m)
                        WAN.append(wan)
            if ("WAN-VRF Data;") not in i:
                WAN.append("none")
    else:
        WAN.append("")
    WAN.pop(0)
    return WAN
