import matplotlib.pyplot as plt
# from blaze.compute.tests.test_numpy_compute import ax

from out_put import log
from gen_sample_data import gen_sample_data
from Linear_Regression import train



def test():
    x_list, y_list = gen_sample_data()
    plt.scatter(x_list, y_list)
    plt.show()


def linear_regression():
    lr = 0.001
    x_list, y_list = gen_sample_data()
    batch_size = 100
    max_iter = 100

    train(x_list, y_list, batch_size, lr, max_iter)


if __name__ == '__main__':
    # test()
    linear_regression()

