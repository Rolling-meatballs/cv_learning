import numpy as np
from out_put import log
from hand_low_medianblur import median

#降低复杂度的方法1
def high_medianblur_1(lay):
    row, colomn = lay.shape
    # log('row', row, 'colomn', colomn)
    j = 0
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
            #初始窗口遍历
            if i == 1 and j == 1:
                a = []
                k = 0
                i_i = i - 1
                j_j = j - 1
                for k in range(3):
                    for d in range(3):
                        s = lay[i_i + k][j_j + d]
                        a.append(s)
                        # log(a)
                j += 1
            #第一行之后的后边缘窗口处理
            elif j == (colomn - 2) and (i % 2) == 0:
                for s in range(6):
                    a[s] = a[s + 3]
                a[6] = lay[i + 1][j - 1]
                a[7] = lay[i + 1][j]
                a[8] = lay[i + 1][j + 1]
                j -= 1
            # 第一行之后的前边缘窗口处理
            elif j == 1 and (i % 2) != 0:
                for s in range(6):
                    a[s] = a[s + 3]
                a[6] = lay[i + 1][j - 1]
                a[7] = lay[i + 1][j]
                a[8] = lay[i + 1][j + 1]
                j += 1
            #偶数行窗口处理，窗口逆向向行进
            elif (i % 2) == 0:
                a[2] = a[1]
                a[5] = a[4]
                a[8] = a[7]
                a[1] = a[0]
                a[4] = a[3]
                a[7] = a[6]
                a[0] = lay[i - 1][j - 1]
                a[3] = lay[i][j - 1]
                a[6] = lay[i + 1][j - 1]
                j -= 1
            #奇数行窗口处理，窗口正向行进
            else:
                a[0] = a[1]
                a[3] = a[4]
                a[6] = a[7]
                a[1] = a[2]
                a[4] = a[5]
                a[7] = a[8]
                a[2] = lay[i - 1][j + 1]
                a[5] = lay[i][j + 1]
                a[8] = lay[i + 1][j + 1]
                j += 1
            # log('a', a)
            middle = median(a)
            # log('middle', middle)
            middle_n.append(middle)
        # i = 340
        # log('middle_n', middle_n)
        end_n = np.append(end_n, [middle_n], axis=0)
    # log('end_n_short', end_n)
    return end_n



