# f(x,y) = x^2+3x+y^2+8y+1
# 对此二维函数的x,y求导

# 函数表达 f(x,y) = x^2+3x+y^2+8y+1
def f_demo(x,y):
    return x**2+3*x+y**2+8*y+1

# 导函数表达,(x,y)对函数f(x,y) = x^2+3x+y^2+8y+1的求导
def df_demo(x,y):
    return 2*x+3,2*y+8

# 设x,y的坐标值为5,5
x,y = 5,5
# 循环迭代,次数30,步长0.1
for it in range(30):
    v_x,v_y=df_demo(x,y)
    x,y=x-0.1*v_x,y-0.1*v_y
    print("f_demo({}{})={}".format(x,y,f_demo(x,y)))
