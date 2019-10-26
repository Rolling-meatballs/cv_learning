import time
import numpy as np
import matplotlib.pyplot as plt

from out_put import log


def sigmoid(w, b, x):
    """
    做一个预测，同过给定一个w、b，之后给出任意一个x，都可以得到一个预测值y
    :param w: 线性回归的斜率，x的系数
    :param b: 与x轴的截距
    :param x: 因变量
    :return: 预测值
    """
    X = w * x + b
    pred_y = 1 / (1 + np.exp(- X))

    return pred_y


def eval_loss(w, b, x_list, gt_y_list):
    """
    cost function, 做一个Loss计算
    :param w: 线性回归的斜率，x的系数
    :param b: 与x轴的截距
    :param x_list: x的集合
    :param gt_y_list: 实际的y值集合
    gt ： ground trues 实际值
    :return: 所有的gt_y和pred_y的方差和
    """
    avg_loss = 0
    for i in range(len(x_list)):
        pred_y = sigmoid(w, b, x_list[i])
        avg_loss += 0.5 * (pred_y - gt_y_list[i]) ** 2
    avg_loss /= len(gt_y_list)
    return avg_loss


def gradient(pred_y, gt_y, x):
    """
    求梯度, 关于w和b
    """
    diff = pred_y - gt_y
    dw = diff * x
    db = diff
    return dw, db


def cal_step_gradient(batch_x_list, batch_gt_y_list, w, b, lr):
    """
    取一部分的数据做计算，其中的x、y 对w、b所带来的更新
    :param batch_x_list: 选取的部分x样本
    :param batch_gt_y_list: 选取的部分y样本
    :param lr: 学习率（阿发）
    :return: 经过一次迭代之后，w、b的值
    """
    avg_dw, avg_db = 0, 0
    batch_size = len(batch_x_list)
    for i in range(batch_size):
        pred_y = sigmoid(w, b, batch_x_list[i])
        dw, db = gradient(pred_y, batch_gt_y_list[i], batch_x_list[i])
        avg_dw += dw
        avg_db += db
    avg_dw /= batch_size
    avg_db /= batch_size
    w -= lr * avg_dw
    b -= lr * avg_db
    return w, b


def train_Regression(x_list, gt_y_list, batch_size, lr, max_iter):
    """

    :param x_list:
    :param gt_y_list:
    :param batch_size: 全部的值
    :param lr: 学习率
    :param max_iter: 迭代次数，要更新的次数
    :return:
    """
    w, b = 0, 0
    num_samples = len(x_list)
    plt.ion()
    fig, ax = plt.subplots()
    for i in range(max_iter):
        # 随机抽取（batch_size)个样本
        batch_idxs = np.random.choice(num_samples, batch_size)
        batch_x = [x_list[j] for j in batch_idxs]
        batch_y = [gt_y_list[j] for j in batch_idxs]
        w, b = cal_step_gradient(batch_x, batch_y, w, b, lr)
        s1 = 'w:{}, b:{}'.format(w, b)
        s2 = 'loss is {}'.format(eval_loss(w, b, x_list, gt_y_list))
        log('s_1', s1, '\n', 's_2', s2)
        ax.cla()
        # time.sleep(1)
    return w, b
