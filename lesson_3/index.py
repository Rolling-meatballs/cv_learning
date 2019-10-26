import matplotlib.pyplot as plt

from out_put import log
from Linear_Regression import train_Linear
from Logistic_Regression import train_Regression
from gen_sample_data import (
    gen_sample_data_Linear,
    gen_sample_data_Logisitic
)



def test():

    clas = 2

    # x_list, y_list = gen_sample_data_Linear()
    x_list, y_list = gen_sample_data_Logisitic(clas)
    # log(x_list)
    # log(y_list)
    plt.scatter(x_list, y_list)
    plt.show()


def linear_regression():
    lr = 0.001
    x_list, y_list = gen_sample_data_Linear()
    batch_size = 100
    max_iter = 100

    train_Linear(x_list, y_list, batch_size, lr, max_iter)


def logisitic_regression():
    clas = 2
    x_list, y_list = gen_sample_data_Logisitic(clas)

    lr = 0.001
    batch_size = 100
    max_iter = 100

    train_Linear(x_list, y_list, batch_size, lr, max_iter)


if __name__ == '__main__':
    # test()
    linear_regression()

