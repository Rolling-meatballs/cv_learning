#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
cv2.__version__


# In[111]:


import matplotlib.pyplot as plt
import random


# In[4]:


import numpy as np


# In[6]:


img = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 1)


# In[13]:


cv2.imshow('woman', img)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


# In[9]:


# to show RPG image to show image matrix


# In[12]:


print(img)


# In[14]:


img_grey = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 0)


# In[16]:


cv2.imshow('woman', img_grey)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


# In[ ]:


# opencv bgr, matplotlib rgb, pillow


# In[17]:


plt.imshow(img)


# In[25]:


B, G, R = cv2.split(img)


# In[29]:


print(B)
print(G)
print(R)


# In[44]:


img_new = cv2.merge((R, G, B))
# print('new',img_new)
plt.imshow(img_new)


# In[45]:


count = 25
R[R>230] = 255
R[R<=230] = R[R<=230] + 25
B, G, R = cv2.split(img)
img_new = cv2.merge((R,B,G))
plt.imshow(img_new)


# In[47]:


B, G, R = cv2.split(img)
img_new = cv2.merge((R, G, B))
plt.imshow(img_new)


# In[56]:


print(img_new.shape)


# # gamma corrention

# In[71]:


img_dark = cv2.imread('D:\OneDrive\cv\couse_1\dark.jpg', 1)
cv2.imshow('woman', img_dark)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


# In[77]:


def gamma_adjust(image, gamma = 1.0):
    invGamma = 1.0 / gamma
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype('uint8')    
    img_gamma = cv2.LUT(image, table)
    return img_gamma


# In[79]:


img_gamma = gamma_adjust(img_dark, gamma = 0.5 )
cv2.imshow('woman', img_gamma)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


# # image crop

# In[80]:


img = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 1)
print(img.shape)


# In[90]:


img_crop = img[100:500,50:550 ]
cv2.imshow('woman', img_crop)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


# In[93]:


img_grey = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 0)
img.flatten().shape


# In[98]:


hist = img_grey.flatten()
plt.hist(hist,256,[0,256])


# In[104]:


img_eq = cv2.equalizeHist(img_grey)
cv2.imshow('woman', img_eq)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()


# # similarity transform

# In[103]:


img_colar = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 1)
M = cv2.getRotationMatrix2D((img_colar.shape[1] / 2, img_colar.shape[0] / 2), 30, 1)
img_rotate = cv2.warpAffine(img_colar, M, (img_colar.shape[1], img_colar.shape[0]))
cv2.imshow('rotated woman', img_rotate)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
    
print(M)


# # Affine Transform

# In[105]:


img_colar = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 1)
rows, cols, ch = img_colar.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('affine woman', dst)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()


# # Perspective Transform

# In[112]:


img_colar = cv2.imread('D:\OneDrive\cv\couse_1\woman.jpg', 1)
def random_warp(img, row, col):
    height, width, channels = img_colar.shape
    
    #warp:
    random_margin = 60
    x1 = random.randint(-random_margin, random_margin)
    y1 = random.randint(-random_margin, random_margin)
    x2 = random.randint(width - random_margin - 1, width - 1)
    y2 = random.randint(-random_margin, random_margin)
    x3 = random.randint(width - random_margin - 1, width - 1)
    y3 = random.randint(height - random_margin - 1, height - 1)
    x4 = random.randint(-random_margin, random_margin)
    y4 = random.randint(height - random_margin - 1, height - 1)

    dx1 = random.randint(-random_margin, random_margin)
    dy1 = random.randint(-random_margin, random_margin)
    dx2 = random.randint(width - random_margin - 1, width - 1)
    dy2 = random.randint(-random_margin, random_margin)
    dx3 = random.randint(width - random_margin - 1, width - 1)
    dy3 = random.randint(height - random_margin - 1, height - 1)
    dx4 = random.randint(-random_margin, random_margin)
    dy4 = random.randint(height - random_margin - 1, height - 1)

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
    M_warp = cv2.getPerspectiveTransform(pts1, pts2)
    img_warp = cv2.warpPerspective(img_colar, M_warp, (width, height))
    return M_warp, img_warp
M_warp, img_warp = random_warp(img_colar, img_colar.shape[0], img_colar.shape[1])
cv2.imshow('woman_warp', img_warp)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()


# In[ ]:




