import os
from threading import Thread
from time import sleep, ctime


def mqtt_server():
    os.system("python ./mqtt_server.py")
def mqtt_clients():
    os.system("python ./mqtt_clients.py")


if __name__=="__main__":
    try:
        print("设备模拟器开始发送消息")
        print("关闭请按Ctrl+C")
        thread_list=[
            Thread(target=mqtt_clients),
            Thread(target=mqtt_server)
        ]
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
    except:
        print("设备模拟器关闭成功")