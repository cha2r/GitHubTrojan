#coding=utf-8
import os
import sys
import time
file = '/root'
def run(**args):
	print "[*]Now in device module"
	files = os.listdir(file)
	# os.path.getatime(file)  # 输出最近访问时间
	# os.path.getctime(file) # 输出文件创建时间
	# os.path.getmtime(file) # 输出最近修改时间
	# time.gmtime(os.path.getmtime(file)) # 以struct_time形式输出最近修改时间
	# os.path.getsize(file)  # 输出文件大小（字节为单位）

	return str(files)
