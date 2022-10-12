import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from matplotlib.pyplot import MultipleLocator
from scipy.interpolate import make_interp_spline

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def err(p, x, y):
    return p[0] * x + p[1] - y

if __name__ == "__main__":
    t = np.array([40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0])
    v = np.array([0.4609, 0.4501, 0.4395, 0.4293, 0.4174, 0.4054, 0.3937, 0.3812, 0.3700, 0.3561 ])

    ret = leastsq(err, np.array([0, 0]), args = (t, v))
    k, b = ret[0]
    x = np.linspace(35, 90, 1000)
    y = k * x + b

    plt.figure(1, figsize =(15, 10), dpi=100)

    # plot scatter and line
    plt.plot(x, y, color="red", label = "拟合曲线", linewidth=2)
    plt.scatter(t, v, label = "原始数据点", s = 100)
    print(f"k = {k}, b = {b}")
    # plot settings
    plt.legend()
    plt.title("If=50μA条件下PN结正向电压随温度的变化特性", fontsize = 24)
    plt.xlabel("温度（°C）", fontsize = 20)
    plt.ylabel("电压（V）", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(0.01))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.ylim(0.35, 0.47)
    plt.xlim(35, 90)


    Vf = np.array([0.3009, 0.3201, 0.3400, 0.3600, 0.3804, 0.4008, 0.4206, 0.4404, 0.4601])
    If = np.array([0.1, 0.2, 0.4, 0.8, 1.5, 2.8, 5.0, 9.2, 15.8])

    plt.figure(2, figsize=(15, 10), dpi = 100)
    plt.scatter(Vf, If, label = "原始数据点", s = 100)
    model = make_interp_spline(Vf, If)
    xs = np.linspace(0.2, 0.5)
    ys = model(xs)
    plt.plot(xs, ys, color = 'red', label = "拟合曲线", linewidth = 2)

    plt.title("常温情况下（22.4°C）PN结正向伏安特性曲线", fontsize = 24)
    plt.xlabel("电压（V）", fontsize = 20)
    plt.ylabel("电流（μA）", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(0.02))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.xlim(0.3, 0.5)
    plt.ylim(0, 18)



    Vf2 = np.array([0.3009, 0.3201, 0.3400, 0.3600, 0.3804, 0.4008, 0.4206, 0.4404, 0.4601])
    If2 = np.array([0.6, 1.1, 2.0, 3.6, 6.3, 11.1, 18.8, 31.8, 50.6])

    plt.figure(3, figsize=(15, 10), dpi = 100)
    plt.scatter(Vf2, If2, label = "原始数据点", s = 100)
    model = make_interp_spline(Vf2, If2)
    xs = np.linspace(0.2, 0.5)
    ys = model(xs)
    plt.plot(xs, ys, color = 'red', label = "拟合曲线", linewidth = 2)

    plt.title("高温情况下（40.0°C）PN结正向伏安特性曲线", fontsize = 24)
    plt.xlabel("电压（V）", fontsize = 20)
    plt.ylabel("电流（μA）", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(0.02))
    ax.yaxis.set_major_locator(MultipleLocator(5))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.xlim(0.3, 0.5)
    plt.ylim(0, 60)

    plt.show()
