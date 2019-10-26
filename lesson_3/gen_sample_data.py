import random


def gen_sample_data():
    """
    生成测试数据
    """
    w = random.randint(0, 10) + random.random()
    b = random.randint(0, 5) + random.random()

    num_pample = 100
    x_list = []
    y_list = []

    for i in range(num_pample):
        x = random.randint(0, 100) * random.random()
        y = w * x + b + random.random() * random.randint(-1, 100)

        x_list.append(x)
        y_list.append(y)

    return x_list, y_list