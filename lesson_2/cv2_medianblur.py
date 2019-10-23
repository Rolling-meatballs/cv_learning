import cv2
from picture_show import (
    Pic,
    Or_show,
    show,
)

#利用opencv进行中值滤波处理
def cv2_medianblur():
    Pic_c = Pic().pic_c()
    md_img = cv2.medianBlur(Pic_c, 7)
    Or_show()
    show(md_img, 'md_woman')