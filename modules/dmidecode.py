#coding=utf-8

from  subprocess  import  Popen, PIPE
import os

def run(**args):
    print "[*]Now in dmidecode module."
    p = Popen(['dmidecode'], stdout=PIPE, stderr=PIPE)
    data = p.stdout.read()
    return str(data)
