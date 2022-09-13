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
    temperature =np.array( [30, 35, 40, 45, 50, 55, 60, 65, 70])
    v =np.array( [0.020, 0.159, 0.312, 0.502, 0.754, 1.011, 1.298, 1.627, 1.978])
    R =np.array( [51.020, 43.146, 35.774, 30.277, 24.808, 20.760, 17.378, 14.688, 12.471])
    ret = leastsq(err, [0, 0], args = (temperature, v))
    k, b = ret[0]
    x = np.linspace(25, 75, 1000)
    y = k * x + b

    plt.figure(1, figsize =(15, 10), dpi=100)

    # plot scatter and line
    plt.plot(x, y, color="red", label = "拟合曲线", linewidth=2)
    plt.text(45, 1.4, r'$V=%.3fR%.3f$'%(k, b), fontsize = 16, color = 'blue' )
    plt.scatter(temperature, v, label = "原始数据点", s = 100)
    print(f"k = {k}, b = {b}")

    # plot settings
    plt.legend()
    plt.title("合金输出电压与合金温度值关系图", fontsize = 24)
    plt.xlabel("温度(°C)", fontsize = 20)
    plt.ylabel("合金输出电压(mV)", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.xlim(20, 80)
    plt.ylim(-0.3, 2.5)


    plt.figure(2, figsize=(15, 10), dpi = 100)
    plt.scatter(temperature, R, label = "原始数据点", s = 100)
    model = make_interp_spline(temperature, R)
    xs = np.linspace(25, 75)
    ys = model(xs)
    plt.plot(xs, ys, color = 'red', label = "拟合曲线", linewidth = 2)

    plt.legend()
    plt.title("半导体电阻与温度的关系", fontsize = 24)
    plt.xlabel("温度(°C)", fontsize = 20)
    plt.ylabel("半导体电阻(kΩ)", fontsize = 20)
    plt.grid()
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(5))
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.xlim(20, 80)
    plt.ylim(0, 60)

    plt.show()
