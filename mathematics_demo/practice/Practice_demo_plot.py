# 画出图像
# f(x,y) = x^2+3x+y^2+8y+1 导数图像

# 函数表达 f(x,y) = x^2+3x+y^2+8y+1
def f_demo(x,y):
    return x**2+3*x+y**2+8*y+1

# 导函数表达,(x,y)对函数f(x,y) = x^2+3x+y^2+8y+1的求导
def df_demo(x,y):
    return 2*x+3,2*y+8


from mpl_toolkits.mplot3d import  Axes3D

import numpy as np

import matplotlib.pyplot as plt

# 坐标设置在-20,20
x=np.linspace(-20,20)
# 坐标设置在-20,20
y=np.linspace(-20,20)

X,Y = np.meshgrid(x,y)

fig=plt.figure()

ax = fig.gca(projection='3d')

surf = ax.plot_surface(X,Y,f_demo(X,Y))

plt.show()