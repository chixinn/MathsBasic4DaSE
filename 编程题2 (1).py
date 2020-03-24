#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections
import os


# In[2]:


num_of_doc=10
tf_words=[]
words=[]


# In[3]:


with open('data.txt')as file:
    for i in range(num_of_doc):
        words=file.readline().split()##统计每篇文章的，按空行分开
        tf_words.append({})
        for word in words:
            if word in tf_words[i]:#如果出现过了
                tf_words[i][word]+=1/len(words)
            else:#如果没有出现
                tf_words[i][word]=1/len(words)
                


# In[4]:


import math
idf_words=[]#新建一个词典
for i in range(num_of_doc):
    idf_words.append({})
    for word in tf_words[i]:#对于i文章的每个单词
        count=0
        for j in range(num_of_doc):#对于每篇文章
            if word in tf_words[j]:#如果有就加1 ，所以不需要break?
                count=count+1;
        idf_words[i][word]=math.log(num_of_doc/count)        
        
    


# In[5]:


tf_idf_words=[]
for i in range(num_of_doc):
    tf_idf_words.append({})
    for word in tf_words[i]:
        tf_idf_words[i][word]=tf_words[i][word]*idf_words[i][word]
        
        


# In[6]:


#csv导出
import pandas as pd
tf=pd.DataFrame(tf_words).fillna(0)
idf=pd.DataFrame(idf_words).fillna(0)
tf_idf=pd.DataFrame(tf_idf_words).fillna(0)
tf.to_csv('tf.csv')
idf.to_csv('idf.csv')
tf_idf.to_csv('tf_idf.csv')


# In[ ]:




