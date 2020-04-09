#!/usr/bin/env python
# coding: utf-8

# In[1]:


#用python将一张图片旋转一定的角度。
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#图像读取
img=np.array(Image.open('sample.jpg'))


# In[2]:


#旋转参数
#旋转角度
theta=30/180*np.pi#30度
cos_theta=np.cos(theta)
sin_theta=np.sin(theta)
#旋转中心点位置
#原图像的点
center_i=len(img)/2
center_j=len(img[0])/2


# In[3]:


#前向变换结果位置
imgr=np.zeros_like(img)#初始化一个维度相同的array
for i in range(len(img)):
    for j in range(len(img[0])):
        yi=int((i-center_i)*cos_theta-(j-center_j)*sin_theta+center_i)
        yj=int((j-center_j)*cos_theta+(i-center_i)*sin_theta+center_j)
        if yi<0 or yj<0 or yi>=len(img) or yj>=len(img[0]):
            continue
        for k in range(3):
            imgr[yi][yj][k]=img[i][j][k]


# In[4]:


#输出结果图像
fig1=plt.figure()
ax=plt.subplot(111)
ax.imshow(imgr)
ax.axis('off')
plt.show()


# In[5]:


#后向变换结果位置
imgR=np.zeros_like(img)#初始化一个维度相同的array
for i in range(len(img)):
    for j in range(len(img[0])):
        xi=int((i-center_i)*cos_theta-(j-center_j)*sin_theta+center_i)
        xj=int((j-center_j)*cos_theta+(i-center_i)*sin_theta+center_j)
        if xi<0 or xj<0 or xi>=len(img) or xj>=len(img[0]):
            continue
        for k in range(3):
            imgR[i][j][k]=img[xi][xj][k]


# In[6]:


#输出结果图像
fig2=plt.figure()
ax=plt.subplot(111)
ax.imshow(imgR)
ax.axis('off')
plt.show()


# In[7]:


#保存结果图像
fig1.savefig('fig1.jpg')
fig2.savefig('fig2.jpg')


# In[8]:


import cv2
import numpy as np
img = cv2.imread('sample.jpg')
cv2.imshow('img',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

height,width,channel=img.shape
new_height,new_width=2*height,2*width
#新设图片
dst=np.zeros((new_height,new_width,3),dtype=np.uint8)

s_1,s_2=height//2,width//2
d_1,d_2=height,width

delta=30
cosd=(np.cos(delta/180*np.pi))
sind=(np.sin(delta/180*np.pi))


# In[9]:


#前向映射
for x_1 in range(0,height):
    for x_2 in range(0,width):
        y_1=int((i-center_i)*cos_theta-(j-center_j)*sin_theta+center_i)
        y_2=int((j-center_j)*cos_theta+(i-center_i)*sin_theta+center_j)
        dst[y_1,y_2]=img[x_1,x_2]
cv2.imshow('dst',dst)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[10]:


#重设图片
dst=np.zeros((new_height,new_width,3),dtype=np.uint8)


# In[11]:


for y_1 in range(0,height):
    for y_2 in range(0,width):
        x_1=int((i-center_i)*cos_theta-(j-center_j)*sin_theta+center_i)
        x_2=int((j-center_j)*cos_theta+(i-center_i)*sin_theta+center_j)
        if height > x_1>=0 and width >x_2>=0:
            dst[y_1,y_2]=img[x_1,x_2]

cv2.imshow('dst',dst)
cv2.waitKey(5000)
cv2.destroyAllWindows()

