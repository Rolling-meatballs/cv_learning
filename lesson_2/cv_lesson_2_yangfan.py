import time
import cv2
from hand_low_medianblur import low_short
from cv2_medianblur import  cv2_medianblur
from high_medianblur_1 import high_medianblur_1
from high_medianblur_2 import high_medianblur_2
from picture_show import (
    Pic,
    Or_show,
    show,
)
from write_txt import read_pic
from out_put import log
import numpy as np

def hand_medianblur(way):
    B, G, R = Pic().pic_RGB()

    # read_pic(B, '1.txt')
    # md_img = cv2.medianBlur(B, 7)
    # read_pic(md_img, 'md_img.txt')
    # l_B = low_medianblur(B)
    l_B = way(B)
    # read_pic(l_B, 'l_B.txt')
    l_G = way(G)
    l_R = way(R)
    # log(B)
    l_img = cv2.merge((l_R, l_G, l_B))
    # show(l_img, 'l_img ')
    # show(l_B, 'l_B_img ')
    # show(R, 'R_img ')

    # show(md_img, 'l_img ')

#高时间复杂度的方法
def hand_low():
    way = low_short
    hand_medianblur(way)

#低时间复杂度的方法1
def hand_high_1():
    way = high_medianblur_1
    hand_medianblur(way)

#低时间复杂度的方法2
def hand_high_2():
    way = high_medianblur_2
    hand_medianblur(way)

#生成小规模数据
def data():
    a = 5
    b = 5
    n = np.zeros((a,b), dtype='int')
    k = 1
    for i in range(a):
        for j in range(b):
            n[i][j] = k
            k += 1

    return n

#小数据测试
def l_test():
    a = data()
    high_medianblur_1(a)

#调用需要测试的函数
def test():

    # cv2_medianblur() #利用opencv的中值滤波函数的操作
    # hand_low() #自己编写的low_lever的中值滤波函数
    hand_high_1()#自己编写的high_lever的中值滤波函数,方法1
    # hand_high_2()#自己编写的high_lever的中值滤波函数,方法2





if __name__ == '__main__':
    time_start = time.time()
    test()
    # l_test()
    time_end = time.time()
    print('totally cost', time_end - time_start)
