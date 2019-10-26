import random

from out_put import log


def gen_sample_data(w_s, w_e, b_s, b_e, x_s, x_e, num_pample, c):
    """
        生成测试数据
        """
    w = random.randint(w_s, w_e) + random.random()
    b = random.randint(b_s, b_e) + random.random()

    x_list = []
    y_list = []

    for i in range(num_pample):
        x = random.randint(x_s, x_e) * random.random() + c
        # x = random.randint(50, 70) * random.random()
        # x = random.randint(50, 70)
        # y = w * x + b + random.random() * random.randint(-1, 100)
        y = w * x + b + random.random() * random.randint(-1, 100) + c / 5

        x_list.append(x)
        y_list.append(y)

    return x_list, y_list


def gen_sample_data_Linear():
    """
    数据生成条件
    """
    # w边界
    w_s = 0
    w_e = 10
    # b边界
    b_s = 0
    b_e = 5

    # 数据规模
    num_pample = 100

    # x范围
    x_s = 0
    x_e = 100

    x_list, y_list = gen_sample_data(w_s, w_e, b_s, b_e, x_s, x_e, num_pample, 0)

    return x_list, y_list


def gen_sample_data_Logisitic(clas):
    """
    数据生成条件
    :clas: 类别数量
    :return:
    """
    # w边界
    w_s = [0] * 4
    w_e = [10, 10, -10, -10]
    # b边界
    b_s = [0] * 4
    b_e = [10] * 4

    # 数据规模
    num_pample = 50

    # x范围
    x_s = [0, 60, 0, 60]
    x_e = [40, 80, 40, 80]

    x_list = []
    y_list = []

    c = [0, 50]

    for i in range(clas):
        log('i', i)
        x, y = gen_sample_data(w_s[i], w_e[i], b_s[i], b_e[i], x_s[i], x_e[i], num_pample, c[i])
        x_list += x
        y_list += y
        # log(x_list)
        # log(y_list)

    return x_list, y_list