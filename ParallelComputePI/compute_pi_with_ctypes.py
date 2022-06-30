import time
import ctypes
import threading
import os
import matplotlib.pyplot as plt
import math

def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return False
    return True

if __name__ == '__main__':

    #items, threads = input("并行计算 PI 值，输入项数和线程数：").split()
    #items = 1e10
    #threads = 4
    #items = ctypes.c_longlong(int(items))
    #threads = ctypes.c_int(int(threads))

    items_list_raw = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10]
    threads_nums_raw = [1, 2, 4, 8, 16]
    threads_average_time_list = []

    items_list = [ctypes.c_longlong(int(items)) for items in items_list_raw]
    threads_nums = [ctypes.c_int(threads) for threads in threads_nums_raw]

    for threads in threads_nums:

        average_time_list = []

        for items in items_list:

            time_list = []

            for epoch in range(5):

                time_start = time.perf_counter()

                libc = ctypes.cdll.LoadLibrary("./libcompute_pi.so")
                libc.compute_pi_c.restype = ctypes.c_longdouble
                pi = libc.compute_pi_c(items, threads)
                
                time_end = time.perf_counter()

                time_list.append((time_end - time_start))

                print(f"第{epoch}次：用 {items.value} 个项和 {threads.value} 个线程并行计算的 PI = {pi}, 用时 {time_end - time_start} 秒.")

            average_time = sum(time_list) / len(time_list)
            average_time_list.append(average_time)

            print(f"用 {items.value} 个项和 {threads.value} 个线程并行计算的 PI = {pi}, 平均用时 {average_time} 秒.")

        threads_average_time_list.append(average_time_list)
    
    data_dir = './Result/'
    check_dir(data_dir)
    items_list_exponent = [math.log10(items) for items in items_list_raw]

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