import os
import matplotlib.pyplot as plt
import math

def check_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return False
    return True

if __name__ == '__main__':

    items_list = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10]
    threads_average_time_list = [
        [0.000144, 0.000062, 0.000044, 0.000178, 0.000950, 0.005041, 0.043867, 0.425254, 4.242543, 42.369809],
        [0.000100, 0.000097, 0.000028, 0.000313, 0.000315, 0.002357, 0.022777, 0.218178, 2.173741, 21.720906],
        [0.000091, 0.000050, 0.000080, 0.000059, 0.000301, 0.002250, 0.014475, 0.114250, 1.124617, 11.179505],
        [0.000173, 0.000125, 0.000137, 0.000158, 0.001033, 0.004010, 0.017246, 0.119800, 1.127788, 11.275935],
        [0.000303, 0.000237, 0.000239, 0.000925, 0.002011, 0.004421, 0.016860, 0.114578, 1.124608, 11.162283]
    ]

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

