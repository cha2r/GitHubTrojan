#coding=utf-8
def device_filter(dev_content):
    """ dev_content显示了设备的名称和信息
        这里通过关键字查找的方式来判断该设备是否是键盘设备
    """
    # 如果设备信息出现中出现了keyboard这个关键词，那么就认为是键盘设备
    print "device info: ", dev_content
    if "keyboard" in dev_content.lower():
        return True
    return False


def find_keyboard_devices(device_filter_func):
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
    return result


def monitor_keyboard(devs):

    # 将名映射到inputDevice对象
    devices = map(InputDevice, devs)
    # dev.fd一个文件描述符， 然后建立一个字典
    devices = {dev.fd: dev for dev in devices}
    return devices
