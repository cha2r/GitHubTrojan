#!/usr/bin/python
#coding=utf-8

import socket

port_number = [135,443,80,8080,4396]
def run(**args):
    for index in port_number:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', index))
        if result == 0:
            print("Port %d is open" % index)
        else:
            print("Port %d is not open" % index)
        sock.close()
        return str(result)
