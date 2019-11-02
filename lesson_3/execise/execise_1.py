import numpy as np
import matplotlib.pyplot as plt

from out_put import log

np.random.seed(125)
sample_num = 1000

x1 = np.random.multivariate_normal([0, 1], [[1, 0.5], [0.5, 1]], sample_num) #多元正太分布
log('x1', x1)
x2 = np.random.multivariate_normal([4, 7], [[1.7, 1.5], [1.5, 1.7]], sample_num)
log('x2', x2)

real_xdata = np.vstack((x1, x2)).astype(np.float32)  #x
log('real_xdata', real_xdata)
real_label = np.hstack((np.zeros(sample_num), np.ones(sample_num)))
log('real_label', real_label)

plt.figure(figsize=(10, 6))
plt.scatter(real_xdata[:, 0], real_xdata[:, 1],
            c=real_label, alpha=.4)
plt.show()
log('---------------------------------------------------------')

def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))

def logistic_regression(datax, label, num_steps, learning_rate):
    real_datax = np.mat(np.insert(datax, 0, 1, axis=1))
    log('real_datax', real_datax)
    real_label = np.mat(label).transpose()  #将一维数组转换为二维数组，并转置
    log('real_label', real_label)
    params = np.ones((np.shape(real_datax)[1], 1))  #生成一个数据为1的，real_xdata行 1 列的二维数组。
    # log('params', params)
    plt.ion() #起到多开窗口的作用
    fig, ax = plt.subplots()
    plt.rcParams['lines.markersize'] = 3
    for step in range(num_steps):
        scores = real_datax * params
        predictions = sigmoid(scores)
        params = params + learning_rate * real_datax.transpose() * (real_label - predictions)
        log('params', params)
        x1_min = np.min(datax[:, 0])
        x1_max = np.max(datax[:, 0])
        x2_min = np.min(datax[:, 1])
        x2_max = np.max(datax[:, 1])
        plt.xlim(x1_min, x1_max)
        plt.ylim(x2_min, x2_max)

        x_line = np.linspace(x1_min, x1_max, 1000)
        y_line = (-params[0, 0] - params[1, 0] * x_line) / params[2, 0]
        plt.plot(x_line, y_line)
        plt.title(str(step) + '--iterations', fontsize='xx-large')
        plt.scatter(real_xdata[:, 0], real_xdata[:, 1],
                    c=label, alpha=.4)
        plt.pause(1)
        ax.cla()
    return params

if __name__ == '__main__':

        logistic_regression(real_xdata, real_label, 1, 0.08)