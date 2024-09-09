import time
import threading
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1) 

if __name__ == '__main__':
    # 唱歌的线程
    sing_thread=threading.Thread(target=sing,args=("唱歌",))# args通过元组传参
    # 跳舞的线程
    dance_thread=threading.Thread(target=dance,kwargs={"msg":"跳舞"})# kwargs通过字典传参
    # 启动线程
    sing_thread.start()
    dance_thread.start()



