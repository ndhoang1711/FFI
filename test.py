

def DETECT_VENDOR(interfaces):
    detect = interfaces.split(" ")
    for i in detect:
        if ("Cisco") in i:
            return 1
        if ("JUNOS") in i:
            return 0

#vendor = 1
#print(vendor)
print(DETECT_VENDOR("JUNOS nalsd"))
