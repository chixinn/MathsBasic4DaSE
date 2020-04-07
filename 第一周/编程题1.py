#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#将图片转化成矩阵
def loadImage():
    im = Image.open("sample.jpg")
    im.show()
    im=im.convert("L")
    data=im.getdata()
    data = np.matrix(data)
    print (data)


# In[3]:


#显示矩阵
loadImage()


# In[18]:


def transposeImage():
    im = Image.open("sample.jpg")
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    plt.imshow(im) # 显示图片
    plt.axis('off') # 不显示坐标轴
    plt.show()
    plt.savefig('sample2.jpg')


# In[20]:


transposeImage()


# In[ ]:




