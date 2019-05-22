#coding=utf-8
import os
import sys
# linux下的系统输入设备信息目录
DEVICES_PATH = '/sys/class/input/'
def run(**args):
    """
        找出所有的键盘设备名
    """
    # 切换到/sys/class/input/这个目录下，类似cd命令
    os.chdir(DEVICES_PATH)
    result = []
    # 遍历/sys/class/input/下的所有的目录
    for each_input_dev in os.listdir(os.getcwd()):
        # 找到设备信息相关的文件
        dev_path = DEVICES_PATH + each_input_dev + '/device/name'
        # 如果这个设备是键盘设备
        if(os.path.isfile(dev_path) and device_filter_func(file(dev_path).read())):
            result.append('/dev/input/' + each_input_dev)
    if not result:
        print("没有键盘设备")
        # 直接结束该进程
        sys.exit(-1)
    return str(result)
