#coding=utf-8
import socket

port_number = [135,443,80,8080,21,23,22,110]
def run(**args):
    temp=[]
    print "[*]Now in port module."
    for index in port_number:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', index))
        if result == 0:
                file  = "Port %d is open" % index
        else:
                file = "Port %d is not open" % index
        temp.append(file)
        
        sock.close()
    
    return str(temp)
