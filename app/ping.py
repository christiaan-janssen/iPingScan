import os

def ping(ip):
    ping = os.popen('ping ' + ip + ' -n 1')
    result = ping.readlines()
    msLine = result[-1].strip()
    return msLine.split(' = ')#[-1]
