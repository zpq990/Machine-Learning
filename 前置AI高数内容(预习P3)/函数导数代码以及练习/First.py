



# 定义 函数 x^2 + 4x +1
def f(x):
    return x ** 2 + 4 * x +1
# 定义 函数的导数 2x +4
def df(x):
    return 2*x + 4
# 给定初始值,再给一个梯度(斜率)进行循环迭代求出最小值
# 梯度值设置为0.1
x_old = 3.14
for it in range(20):
    x_new = x_old - 0.1 * df(x_old)
    x_old = x_new
    print("1f({})={}".format(x_new,f(x_new)))
# 结果集如下
# f(2.112)=13.908544000000001
# f(1.2896)=7.82146816
# f(0.63168)=3.9257396224
# .............................
# f(-1.9259247933290102)=-2.99451286375665
# f(-1.940739834663208)=-2.996488232804256

# 迭代次数增加到200次
x_old = 3.14
for it in range(200):
    x_new = x_old - 0.1 * df(x_old)
    x_old = x_new
    print("2f({})={}".format(x_new,f(x_new)))

# 结果集 可得治在-2时就能获取到函数的最小值-3
# f(2.112)=13.908544000000001
# ...
# f(-1.9999999999999996)=-3.0
# f(-1.9999999999999996)=-3.0

# 梯度参数修改,选取不同的参数进行分别程序运算
# 梯度参数选用0.5
x_old = 3.14
for it in range(20):
    x_new = x_old - 0.5 * df(x_old)
    x_old = x_new
    print("T0.5_f({})={}".format(x_new,f(x_new)))
# T0.5_f(-2.0000000000000004)=-3.0
# T0.5_f(-2.0)=-3.0
# T0.5_f(-2.0)=-3.0
# ................
# T0.5_f(-2.0)=-3.0
# T0.5_f(-2.0)=-3.0
# 梯度参数选用1
x_old = 3.14
for it in range(20):
    x_new = x_old - 1 * df(x_old)
    x_old = x_new
    print("T1_f({})={}".format(x_new,f(x_new)))
# T1_f(-7.140000000000001)=23.419600000000003
# T1_f(3.1400000000000006)=23.419600000000006
# .............................
# T1_f(-7.140000000000001)=23.419600000000003
# T1_f(3.1400000000000006)=23.419600000000006
# 梯度参数选用5
x_old = 3.14
for it in range(20):
    x_new = x_old - 5 * df(x_old)
    x_old = x_new
    print("T_5f({})={}".format(x_new,f(x_new)))
# T_5f(-48.260000000000005)=2136.9876000000004
# T_5f(414.34000000000003)=173335.99560000002
# .............................................
# T_5f(-6.943377828839182e+18)=4.821049567401552e+37
# T_5f(6.249040045955264e+19)=3.9050501495952563e+39
# 结论,梯度发散的过程,产生最重要的因素是因为在迭代中的"步长"进行迭代