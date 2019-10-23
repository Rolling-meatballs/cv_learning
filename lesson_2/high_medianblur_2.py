import numpy as np
from out_put import log
from picture_show import (
    Pic,
)


#降低复杂度的方法1
def high_medianblur_2(lay):
    row, colomn = lay.shape
    log('row', row, 'colomn', colomn)
    i = 1
    j = 1
    end_n = np.empty(shape=[0, colomn - 2], dtype=int)
    while i < (row - 1):
            while j < (colomn - 1):
                a = []
                if i == 1 & j == 1:
                    k = 0
                    i_i = i - 1
                    j_j = j - 1
                    while k < 3:
                        d = 0
                        while d < 3:
                            s = lay[i_i + k][j_j + d]
                            a.append(s)
                            # log(a)
                            d += 1
                        k += 1
                    j += 1
                elif (j == (colomn - 2) & (i % 2) == 0) | (j == 1 & (i % 2 != 0)):
                    for s in range(6):
                        a[s] = a[s + 3]
                        s += 1
                    a[6] = lay[i + 1][j - 1]
                    a[7] = lay[i + 1][j]
                    a[8] = lay[i + 1][j + 1]
                elif (i % 2) == 0:

                    # 对图像进行处理后输出_high
                    def hand_high_medianblur_1():
                        B, G, R = Pic().pic_RGB()

                        high_medianblur(B)