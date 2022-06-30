# ParallelComputePI

本项目介绍了使用 ctypes 库实现 Python 调用 C 编译的动态链接库并行计算 PI 值的方法。并对比了纯 Python、Python threading、ctypes 和 纯 C 四种实现方法的效率。

## 项目文件

- [compute_pi_with_python.py](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_python.py): 纯 Python 实现方法的 Python 代码。

- [compute_pi_with_threading.py](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_threading.py): Python threading 实现方法的 Python 代码。

- [compute_pi_with_ctypes.py](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_ctypes.py): ctypes 实现方法的 Python 代码。

- [compute_pi_with_ctypes.c](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_ctypes.c): ctypes 实现方法的 C 代码。

- [compute_pi_with_ctypes.shell](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_ctypes.shell): `compute_pi_with_ctypes.c` 的编译命令。

- [libcompute_pi.so](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/libcompute_pi.so): `compute_pi_with_ctypes.c` 的编译结果。

- [compute_pi_with_c.c](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_c.c): 纯 C 实现方法的代码。

- [compute_pi_with_c.shell](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_c.shell): `compute_pi_with_c.c` 的编译命令。

- [compute_pi_with_c.out](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/compute_pi_with_c.out): `compute_pi_with_c.c` 的编译结果。

- [plot_compute_pi_with_c.py](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/plot_compute_pi_with_c.py): 绘制 `compute_pi_with_c.out` 的运行结果。 

- [Result](https://github.com/LuYF-Lemon-love/SimpleProject/tree/main/ParallelComputePI/Result): 结果目录

   - [Result/c_result.md](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/Result/c_result.md): 纯 C 实现方法的结果。
   - ![](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/Result/c_result.md)

   - [Result/compute_pi_with_python.png](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/Result/compute_pi_with_python.png): 纯 Python 实现方法的结果。

   - [Result/compute_pi_with_threading.png](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/Result/compute_pi_with_threading.png): Python threading 实现方法的结果。

   - [Result/compute_pi_with_ctypes.png](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/Result/compute_pi_with_ctypes.png): ctypes 实现方法的结果。

   - [Result/plot_compute_pi_with_c.png](https://github.com/LuYF-Lemon-love/SimpleProject/blob/main/ParallelComputePI/Result/plot_compute_pi_with_c.png): 纯 C 实现方法的结果。
   
