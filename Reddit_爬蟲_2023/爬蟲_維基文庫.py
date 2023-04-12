# -*- coding: utf-8 -*-
"""
Created on Sat 4/11 2023

@author: a4691


爬蟲 維基文庫

在reddit上用關鍵字找文章

範例程式:
https://github.com/Fitzy1293/redditsfinder/blob/master/redditsfinder/redditsfinder_utils.py
    
    
API:
    
https://github.com/pushshift/api


"""

# coding:utf-8



import requests
import time
import re
from bs4 import BeautifulSoup
import csv
import os

from opencc import OpenCC


def get_web_page(url):  # 此篇不用這個函式
    resp = requests.get(
        url=url,
        #cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text



def get_context(p): # 取得文章內容
    
    
  #  match = re.search('標題</span><span class="article-meta-value">(\Z|\S|\s|\n|.)*', k)
    

   
    context=p.split('<tbody>',1)
  
    context=context[1].split('NewPP limit report',1)
    
    h=''
    h+='\n\ntitle='+title[0]+'\n\n'
    
    h+='\n\n正文:\n\n'+context[0]+'\n\n'
    
  #  ar = p.replace('<div class="article-metaline"><span class="article-meta-tag">', '\n')  
    
       
    return h


'''

sort_type:
"score", "num_comments", "created_utc"

sort:
"asc", "desc"


http://api.pushshift.io/reddit/search/comment?subreddit:23andme&q:%20Khmer&size:5
    
'''


url = ''


url='https://zh.wikisource.org/wiki/%E5%AE%8B%E6%9B%B8/%E5%8D%B71'# 宋書
url = 'https://zh.wikisource.org/wiki/%E6%99%89%E6%9B%B8/%E5%8D%B7001' #晉書

url='https://zh.wikisource.org/wiki/%E5%BE%8C%E6%BC%A2%E6%9B%B8/%E5%8D%B723'#後漢書

url='https://zh.wikisource.org/wiki/%E4%B8%89%E5%9C%8B%E5%BF%97/%E5%8D%B701' #三國志

url='https://zh.wikisource.org/wiki/%E5%8D%97%E9%BD%8A%E6%9B%B8/%E5%8D%B71' #南齊書

url='https://zh.wikisource.org/wiki/%E6%A2%81%E6%9B%B8/%E5%8D%B701'#梁書

url='https://zh.wikisource.org/wiki/%E6%BC%A2%E6%9B%B8/%E5%8D%B7001%E4%B8%8A' #漢書

url='https://zh.wikisource.org/wiki/%E5%8C%97%E5%8F%B2/%E5%8D%B7001' #北史

#https://api.pushshift.io/reddit/search/submission

fn=0
print('\n\n取得今日維基文庫之文章')

use=''

for i in range(185):
    
  
   # current_page = get_web_page(URL + '')
    
   
   # current_page =  requests.get(url, params={'subreddit':'23andme','author': user, 'size': 10})
    
    current_page =  requests.get(url) #Integer <= 500 最多條目數
   
    p=current_page.text
    
    h=''
    record=''
    
    cc = OpenCC('s2t') # 簡轉繁
    p=cc.convert(p)
   # h+=p+'\n\n\n\n'
   
    
    title = p.split('<title>',1)
    title= title[1].split('</title>')
    
   # print('\ntitle='+title[0]+'\n')
    
    record+='\n\n\ntitle='+title[0]+'\n\n'
    
    test=p.split('<tbody>',1)
    if len(test)<2:
        break
    
    context=get_context(p)   
   
    
    find=context.split('閩') # 搜尋字彙   
    find2=context.split('閩本') # 搜尋字彙   
    num2=0
    num2=len(find2)-1
    num=len(find)-1-num2
    
    record+='詞彙出現次數='+str(num)+'\n\n'
    print()
    
    
    p=p.replace('align="right"', 'align:right')
    
    link=p.split('align:right',1)
    link=link[1].split('</a>',1)
    
    real_link=link=link[0].split('<a href="',1)
    real_link=real_link[1].split('" title',1)
    real_link='https://zh.wikisource.org/'+real_link[0]
    
    record+=url
    
    
    print(record)
    
    h+=context+'\n\n\n----\n\n'
    
    url=real_link
    
    if num>0:
        use+=record
        
        
    
use=use.replace('\\n', '\n')
    
f = open('維基文庫.txt','w', encoding='UTF-8')
   # gg=p.find('Results')
   # p = p.replace('bro is majestic', '\n\n*********************\n\n\n\n\n\n****************\n\n')   
f.write(use)
f.close()
    
  #  print('出現次數='+str(gg))
    

   

print('\n\n-------------------------------\n\n')

print('result:\n\n')

print(use)
print('\n\nend')






