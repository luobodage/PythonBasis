import threading

tickets, lock = 10, threading.Lock()


class ticket(threading.Thread):
    def __init__(self, window_name):
        threading.Thread.__init__(self)
        self.window_name = window_name

    def run(self):
        sell_tickets(self.window_name)


def sell_tickets(thread_name):
    global tickets
    while tickets > 0:
        lock.acquire()  # 加一个同步锁
        if tickets > 0:
            print("----------------------------------")
            print(thread_name, "准备出票，还剩余票：", tickets, "张")
            tickets -= 1
            print(thread_name, "卖出1张车票，还剩：", tickets, "张")
            print("----------------------------------")
        else:
            print("车票卖没啦~")
        lock.release() 


if __name__ == '__main__':
    w1 = ticket("1号窗口")
    w2 = ticket("2号窗口")
    w3 = ticket("3号窗口")
    w1.start()
    w2.start()
    w3.start()
    w1.join()
    w2.join()
    w3.join()
    print("退出主线程")
