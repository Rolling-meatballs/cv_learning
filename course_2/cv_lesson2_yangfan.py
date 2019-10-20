import time
import cv2
import numpy as np


name = 'woman'

# 带有时间的打印函数，可以替代print
def log(*args, **kwargs):
    time_format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    formatted = time.strftime(time_format, value)
    print(formatted, *args, **kwargs)

#将照品显示出来
def show(img, name):
    cv2.imshow(name, img)
    key = cv2.waitKey()
    if key == 27:
        cv2.destroyAllWindows()

#图像读取函数
class Pic(object):
    def __init__(self):
        self.path = 'woman.jpg'

    def pic_c(self):
        img_c = cv2.imread(self.path, 1)
        return img_c

    def pic_g(self):
        img_g = cv2.imread(self.path, 0)
        return img_g

    def pic_RGB(self):
        B, G, R = cv2.split(self.pic_c())
        return B, G, R

#利用opencv进行中值滤波处理
def cv2_medianblur():
    md_img = cv2.medianBlur(Pic().pic_c(), 7)
    show(Pic().pic_c(), name)
    show(md_img, name)

#将含有9个数的数组中的值排序，并其中间值
def median(list):
    order_list = sorted(list)
    # log('order_list', order_list)
    md = order_list[5]
    return md

#自定义中值滤波（2N）
def low_short(lay):
    # value1 = time.localtime(int(time.time()))
    row = len(lay)
    colomn = len(lay[0])
    # log(lay[0])
    # log(colomn)
    # log(row)
    i = 0
    end_n = np.empty(shape=[0, colomn - 2], dtype=int)
    while i < (row - 2):
        middle_n = []
        j = 0
        while j < (colomn - 2):
            a = []
            a.append(lay[i][j])
            # log(a)
            k = 0
            while k < 3:
                d = 0
                while d < 3:
                    s = lay[i + k][j + d]
                    a.append(s)
                    # log(a)
                    d += 1
                k += 1
            middle = median(a)
            # log('middle', middle)
            middle_n.append(middle)
            j += 1
            # log('middle_n', middle_n)
            # log(j)
        i += 1
        # i = 340
        # log('middle_n', middle_n)
        end_n = np.append(end_n, [middle_n], axis=0)
        # log(i)
        # log('end_n', end_n)
    log('end_n_short', end_n)
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

#将图片的数组写入txt文档，方便纠错
def read_pic(lay, name):
    # np.savetxt('data.txt', lay)
    # row = len(lay)
    # log(name)
    file_handle = open(name, mode='w')

    for i in lay:
        # data = str(lay[i])
        # all_data = data + '/n'
        # file_handle.write(all_data)
        i = str(i).strip('[').strip(']').replace(',', '').replace('\'', '') + '\n'
        file_handle.writelines(i)
    file_handle.close()



#对图像进行处理后输出
def hand_low_medianblur():
    B, G, R = Pic().pic_RGB()

    # read_pic(B, '1.txt')
    # md_img = cv2.medianBlur(B, 7)
    # read_pic(md_img, 'md_img.txt')
    # l_B = low_medianblur(B)
    l_B = low_short(B)
    read_pic(l_B, 'l_B.txt')
    # l_G = low_short(G)
    # l_R = low_short(R)
    log(B)
    # l_img = cv2.merge((l_R, l_G, l_B))
    # show(l_img, 'l_img ')
    show(l_B, 'l_B_img ')
    # show(R, 'R_img ')

    # show(md_img, 'l_img ')


#调用需要测试的函数
def test():
    # cv2_medianblur() #利用opencv的中值滤波函数的操作
    hand_low_medianblur() #自己编写的中值滤波函数


if __name__ == '__main__':
    test()
