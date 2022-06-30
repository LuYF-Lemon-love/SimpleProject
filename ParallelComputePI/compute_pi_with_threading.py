import time
import threading
import os
import matplotlib.pyplot as plt
import math

def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return False
    return True

class myThread (threading.Thread):
    
    def __init__(self, threadID, name, items, threads):
        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.items = items
        self.threads = threads
        self.local_pi = 0.0
    
    def run(self):

        piece = int(self.items / self.threads)
        start = self.threadID * piece
        end = start + piece
        factor = 1.0

        if (start % 2 == 0):
            factor = 1.0
        else:
            factor = -1.0

        for i in range(start, end):
            self.local_pi += factor/(2 * i + 1)
            factor = -factor

if __name__ == '__main__':

    #pi = 0.0
    
    #items, threads = input("并行计算 PI 值，输入项数和线程数：").split()
    #items = 1e6
    #threads = 4
    #items = int(items)
    #threads = int(threads)

    threads_nums = [1, 2, 4, 8, 16]
    items_list = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    threads_average_time_list = []

    for threads in threads_nums:

        average_time_list = []

        for items in items_list:

            time_list = []
            items = int(items)

            for epoch in range(5):

                pi = 0.0

                time_start = time.perf_counter()

                threads_list = []

                for i in range(threads):
                    thread_name = "Thread-" + str(i)
                    thread = myThread(i, thread_name, items, threads)
                    threads_list.append(thread)
    
                for thread in threads_list:
                    thread.start()

                for thread in threads_list:
                    thread.join()
                    pi += 4.0 * thread.local_pi
    
                time_end = time.perf_counter()

                time_list.append((time_end - time_start))

                print(f"第{epoch}次：用 {items} 个项和 {threads} 个线程并行计算的 PI = {pi}, 用时 {time_end - time_start} 秒.")
            
            average_time = sum(time_list) / len(time_list)
            average_time_list.append(average_time)

            print(f"用 {items} 个项和 {threads} 个线程并行计算的 PI = {pi}, 平均用时 {average_time} 秒.")

        threads_average_time_list.append(average_time_list)

    data_dir = './Result/'
    check_dir(data_dir)
    items_list_exponent = [math.log10(items) for items in items_list]

    plt.plot(items_list_exponent, threads_average_time_list[0], 'b*-', label='threads_1')
    plt.plot(items_list_exponent, threads_average_time_list[1], 'gp-', label='threads_2')
    plt.plot(items_list_exponent, threads_average_time_list[2], 'rv:', label='threads_4')
    plt.plot(items_list_exponent, threads_average_time_list[3], 'c2:', label='threads_8')
    plt.plot(items_list_exponent, threads_average_time_list[4], 'ys-', label='threads_16')
    
    plt.xlabel("log10(items)")
    plt.ylabel("Average time of five times")
    plt.legend(loc='upper left')
    plt.savefig(data_dir + __file__.split("/")[-1].split(".")[0] + ".png")
    plt.show()  

