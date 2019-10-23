import numpy as np
from out_put import log
from picture_show import (
    Pic,
)

#创建排序数组
def array():
    count = [0] * 255
    return count

#计数增加
def count_add(number, count):
    count[number - 1] += 1
    return count

#计数减少
def count_minus(number, count):
    count[number - 1] -= 1
    return count

#求中间值
def median(count):
    number = 0
    i = 0
    while number < 5:
        number = number + count[i]
        i += 1
    m_number = i
    return m_number



#降低复杂度的方法2
def high_medianblur_2(lay):
    row, colomn = lay.shape
    # log('row', row, 'colomn', colomn)
    j = 1
    count = array()
    end_n = np.empty(shape=[0, colomn - 2], dtype=int)
    for i in range(1, row - 1):
        # log('row', i)
        middle_n = []
        if j == 0:
            j += 1
        elif j == (colomn - 1):
            j -= 1
        while j > 0 and j < (colomn - 1):
            # log('colomn', j)
            if i == 1 and j == 1:
                i_i = i - 1
                j_j = j - 1
                for k in range(3):
                    for d in range(3):
                        s = lay[i_i + k][j_j + d]
                        count = count_add(s, count)
                j += 1
            # 第一行之后的后边缘窗口处理
            elif j == (colomn - 2) and (i % 2) == 0:
                j_j = j - 1
                for s in range(3):
                    count = count_minus(lay[i - 2][j_j + s], count)
                    count = count_add(lay[i + 1][j_j + s], count)
                j -= 1
            # 第一行之后的前边缘窗口处理
            elif j == 1 and (i % 2) != 0:
                j_j = j - 1
                for s in range(3):
                    count = count_minus(lay[i - 2][j_j + s], count)
                    count = count_add(lay[i + 1][j_j + s], count)
                j += 1
            # 偶数行窗口处理，窗口逆向向行进
            elif (i % 2) == 0:
                i_i = i - 1
                for s in range(3):
                    count = count_minus(lay[i_i + s][j + 2], count)
                    count = count_add(lay[i_i + s][j - 1], count)
                j -= 1
            # 奇数行窗口处理，窗口正向行进
            else:
                i_i = i - 1
                for s in range(3):
                    count = count_minus(lay[i_i + s][j - 2], count)
                    count = count_add(lay[i_i + s][j + 1], count)
                j += 1
            middle = median(count)
            # log('middle', middle)
            middle_n.append(middle)
        # i = 340
        # log('middle_n', middle_n)
        end_n = np.append(end_n, [middle_n], axis=0)
    # log('end_n_short', end_n)
    return end_n

