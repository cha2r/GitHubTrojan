# coding=utf-8
import os
import sys


def run(**args):
	print "[*]Now in device module"
	files = os.listdir('/root')

	return str(files)
