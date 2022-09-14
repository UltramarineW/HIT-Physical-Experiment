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
    v = np.array([1.000, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4])
    a = np.array([0.6438, 0.7705, 0.9013, 1.0348, 1.1485, 1.2949, 1.4179, 1.5481])

    ret = leastsq(err, np.array([0, 0]), args = (a, v))
    k, b = ret[0]
    x = np.linspace(0, 2.6, 1000)
    y = k * x + b

    plt.figure(1, figsize =(15, 10), dpi=100)

    # plot scatter and line
    plt.plot(x, y, color="red", label = "拟合曲线", linewidth=2)
    # plt.text(45, 1.4, r'$V=%.3fR%.3f$'%(k, b), fontsize = 16, color = 'blue' )
    plt.scatter(a, v, label = "原始数据点", s = 100)
    print(f"k = {k}, b = {b}")
    print(f"定值电阻的阻值为{k * 1000 - 150}Ω")

    # plot settings
    plt.legend()
    plt.title("电流与电压关系图", fontsize = 24)
    plt.xlabel("电流(mA)", fontsize = 20)
    plt.ylabel("电压(V)", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.ylim(0.8, 2.6)
    plt.xlim(0.5, 1.6)

    diode_a = np.array([0.1270, 0.9065, 1.7448, 4.711, 7.298, 10.152, 12.410, 15.910, 17.434, 18.918])
    diode_v = np.array([1.7080, 1.7956, 1.8313, 1.8984, 1.9312, 1.9567, 1.9718, 1.9930, 1.9968, 2.0009])


    plt.figure(2, figsize=(15, 10), dpi = 100)
    plt.scatter(diode_a, diode_v, label = "原始数据点", s = 100)
    model = make_interp_spline(diode_a, diode_v)
    xs = np.linspace(0, 20)
    ys = model(xs)
    plt.plot(xs, ys, color = 'red', label = "拟合曲线", linewidth = 2)

    plt.title("发光二极管电压与电流关系", fontsize = 24)
    plt.xlabel("电流(mA)", fontsize = 20)
    plt.ylabel("电压(V)", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.xlim(0, 20)
    plt.ylim(1.5, 2.2)

    plt.show()
