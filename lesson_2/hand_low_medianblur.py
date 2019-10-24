import numpy as np
from out_put import log


#将含有9个数的数组中的值排序，并取其中间值
def median(list):
    order_list = sorted(list)
    # log('order_list', order_list)
    md = order_list[4]
    return md

#自定义中值滤波，高时间复杂度的方法
def low_short(lay):
    # value1 = time.localtime(int(time.time()))
    row = len(lay)
    colomn = len(lay[0])
    # log(lay[0])
    # log(colomn)
    # log(row)
    end_n = np.empty(shape=[0, colomn - 2], dtype=int)
    for i in range(row - 2):
        middle_n = []
        for j in range(colomn - 2):
            a = []
            # log(a)
            for k in range(3):
                for d in range(3):
                    s = lay[i + k][j + d]
                    a.append(s)
                    # log(a)
            middle = median(a)
            # log('middle', middle)
            middle_n.append(middle)
            # log('middle_n', middle_n)
            # log(j)
        # i = 340
        # log('middle_n', middle_n)
        end_n = np.append(end_n, [middle_n], axis=0)
        # log(i)
        # log('end_n', end_n)
    # log('end_n_short', end_n)
    # value2 = time.localtime(int(time.time()))
    # value = value2 - value1
    # # time_format = '%Y/%m/%d %H:%M:%S'
    # time_format = '%H:%M:%S'
    # formatted = time.strftime(time_format, value)
    # log(formatted)
    return end_n


# def low_medianblur(lay):
#     shot = low_short(lay)
#     row = len(shot)
#     colomn = len(shot[0])
#     end_n = np.empty(shape=[0, int(colomn * 3)], dtype=int)
#     log(colomn * 3)
#     for r in range(row):
#         a = 0
#         middle = []
#         for i in range(colomn):
#             for j in range(3):
#                 middle.append(lay[r][i])
#                 j += 1
#                 a += 1
#                 log('new_j', j)
#                 log('new_a', a)
#                 log('new_middle', middle)
#             i += 1
#         for k in range(3):
#             end_n = np.append(end_n, [middle], axis=0)
#         r += 1
#         # break
#     log('end_n', end_n)
#     return end_n


#对图像进行处理后输出_low


#计数排序
# def sort(number):
#     max = 255