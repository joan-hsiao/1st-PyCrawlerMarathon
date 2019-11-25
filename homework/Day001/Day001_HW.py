
# coding: utf-8

# # 資料來源與檔案存取
# 
# * 資料來源與取得
# * 開放資料
# * 資料儲存格式
# * Python 存取檔案

# ## 作業目標
# 
# * 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
# * 2.（實作）完成一個程式，需滿足下列需求：
#     * 下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
#     * 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
#     * 將「Hello World」字串覆寫到 Homework.txt 檔案
#     * 檢查 Homework.txt 檔案字數是否符合 Hello World 字數
# 

# ### 1.（簡答題）檔案、API、爬蟲三種取得資料方式有什麼不同？
#     Ans. 
#         1.檔案: 資料會包成標準格式提供下載
#         2.API: 可以選取要讀取的特定部分，而不需整批資料完整下載
#         3.網頁爬蟲: 當資料沒有以前面兩者提供，但出現在網頁上，就可以利用爬蟲程式下載需要的資料

# ### 2.（實作）完成一個程式，需滿足下列需求：
#     * 下載指定檔案到 Data 資料夾，存成檔名 Homework.txt
#     * 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案
#     * 將「Hello World」字串覆寫到 Homework.txt 檔案
#     * 檢查 Homework.txt 檔案字數是否符合 Hello World 字數
# 

# In[1]:


# 根據需求引入正確的 Library

from urllib.request import urlretrieve
import os


# In[2]:


# 下載檔案到 Data 資料夾，存成檔名 Homework.txt

try:
    os.makedirs( './Data', exist_ok=True )
    '''
    Your Code
    '''
except:
    print('發生錯誤！')


# In[3]:


# 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案

files = []

'''
Your Code
'''

if 'Homework.txt' in files:
    print('[O] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')
else:
    print('[X] 檢查 Data 資料夾是否有 Homework.txt 檔名之檔案')


# In[4]:


# 將「Hello World」字串覆寫到 Homework.txt 檔案

f = ''

with open("./Data/Homework.txt", "w") as fh:
    '''
    Your Code
    '''

try:
    with open("./Data/Homework.txt", "r") as fh:
        '''
        Your Code
        '''
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    pass    
    


# In[5]:


# 檢查 Homework.txt 檔案字數是否符合 Hello World 字數

if len('Hello World') == len(f):
    print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
else:
    print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')

