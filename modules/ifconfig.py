#coding=utf-8

from  subprocess  import  Popen, PIPE

def  run(**args):
        print "[*]Now in ifconfig module."
    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read()
    return str(data)
