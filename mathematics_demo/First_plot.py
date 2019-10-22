# 将First中的函数展现到图表上来显示
def f(x):
    return x ** 2 + 4 * x + 1
def df(x):
    return 2 * x +4
x_old = 3.14
for it in range(20):
    x_new = x_old - 0.1 * df(x_old)
    x_old = x_new
    print(x_new,f(x_new))

# 矩阵运算库
import numpy as np
# 可视化库
import matplotlib.pyplot as plt
# 定义域为:-6,3之间产生现象变化的50个数,默认设置的数值是50个
x = np.linspace(-6,3)
# 画出函数的坐标
plt.plot(x,f(x))
# 展示页面图
plt.show()