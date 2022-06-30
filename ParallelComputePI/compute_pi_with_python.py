import time
import os
import matplotlib.pyplot as plt
import math

def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return False
    return True

if __name__ == '__main__':

    #items = input("并行计算 PI 值，输入项数：").split()
    #items = 1e4
    #items = int(items)

    items_list = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    average_time_list = []

    for items in items_list:

        time_list = []

        for epoch in range(5):

            time_start = time.perf_counter()

            factor = 1.0
            pi = 0.0
            for i in range(int(items)):
                pi += factor/(2 * i + 1)
                factor = -factor
    
            pi *= 4
    
            time_end = time.perf_counter()

            time_list.append((time_end - time_start))

            print(f"第{epoch}次：用 {items} 个项计算的 PI = {pi}, 用时 {time_end - time_start} 秒.")
        
        average_time = sum(time_list) / len(time_list)
        average_time_list.append(average_time)

        print(f"用 {items} 个项计算的 PI = {pi}, 平均用时 {average_time} 秒.")
    
    data_dir = './Result/'
    check_dir(data_dir)
    items_list_exponent = [math.log10(items) for items in items_list]
    plt.plot(items_list_exponent, average_time_list, 'b*-')
    plt.xlabel("log10(items)")
    plt.ylabel("Average time of five times")
    plt.legend(loc='upper left')
    plt.savefig(data_dir + __file__.split("/")[-1].split(".")[0] + ".png")
    plt.show()        