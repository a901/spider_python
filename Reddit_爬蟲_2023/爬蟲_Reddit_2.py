# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:08:55 2023

@author: a4691


Reddit 爬蟲

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





def get_context(k): # 取得文章內容
    
    
  #  match = re.search('標題</span><span class="article-meta-value">(\Z|\S|\s|\n|.)*', k)
    
    arr = k.split('標題</span><span class="article-meta-value">')
    ar2= arr[1].split('<span class="f2">※ 發信站: 批踢踢實業坊(ptt.cc), 來自')
    
    ar=ar2[0]
    
    ar = ar.replace('<div class="article-metaline"><span class="article-meta-tag">', '\n')  
    
    ar = ar.replace('<span class="f6">', ': ')
    ar = ar.replace('</span>', '')
    ar = ar.replace('<div class="richcontent">', '\n')
    ar = ar.replace('</div>', '')    
    ar = ar.replace('</a>', '\n')        
    return ar


'''

sort_type:
"score", "num_comments", "created_utc"

sort:
"asc", "desc"


http://api.pushshift.io/reddit/search/comment?subreddit:23andme&q:%20Khmer&size:5
    
'''


url = 'https://api.pushshift.io/reddit/search/comment'
url = 'https://api.pushshift.io/reddit/search/submission'

#https://api.pushshift.io/reddit/search/submission

fn=0
if __name__ == '__main__':
    
    print('取得今日reddit文章')
   # current_page = get_web_page(URL + '')
    
    user='k19911111'
   # current_page =  requests.get(url, params={'subreddit':'23andme','author': user, 'size': 10})
    
    current_page =  requests.get(url, params={ #'subreddit':'23andme',
                                              
                                              'q': 'khmer',   #關鍵字
                                              
                                              #'title':'yi' or 'naxi',
                                             # 'title':'banana apple water',
                                             # 'sort_type':'score' ,
                                              'size':35}) #Integer <= 500 最多條目數
   
   
   
    p=current_page.text
    
    #print(p)
    
    
    pp=p.split('{"subreddit"')
    
    print("pp數量="+str(len(pp)))
    
    h=''
   # h+=p+'\n\n\n\n'
    
    z=0
    num=0
    for x in pp:
        if z==0:
            z+=1
            continue
    
        g=x.split(',"selftext":',1 )#|,"can_gild
        
        if len(g)<2:
            break
        g[1]=g[1].replace(',"gilded"', ',"author_fullname"')
        context=g[1].split(',"author_fullname"',1)
        
        title=context[1].split('"title":',1)
        title=title[1].split('"link_flair_richtext"')
        
        h+='\n\n\n文章'+str(num+1)+':\n\n'
        
        h+=context[0]+'\n\n\n'
        
        h+='------\n\n'
        h+='title:'+title[0]+'\n\n'
        h+='Subreddit'+g[0]+'\n\n'
       # x=x.replace('can_gild','top_awarded_type')
        link=g[1].split('"permalink":"',1)
        link=link[1].split('","parent_whitelist_status',1)
        
        link0='https://www.reddit.com'+link[0]
        
        time=g[1].split('"utc_datetime_str":"',1)
        time=time[1].split('"}')
        
        h+=time[0]+'\n\n'
        
        h+=link0+'\n\n'
        
      #  h+= g[1]+'\n\n'  # test
        
        
       


        gg=g[0]
     #   h+='\n\n\n\n留言'+str(num+1)+':\n\n'+gg
        
        
        '''
        score=g[1].split('score":')
        score= score[1].split('"all_awardings"')
        '''
       
       # h+='\n\n連結:\n'+'https://www.reddit.com'+gh[0]+'\n\n時間:\n'+g2[0]+'\n\n'
        
        z+=1
        num+=1
       
    
    
    print('留言數='+str(num))
    
    h=h.replace('\\n', '\n')
    
    f = open('文章.txt','w', encoding='UTF-8')
   # gg=p.find('Results')
   # p = p.replace('bro is majestic', '\n\n*********************\n\n\n\n\n\n****************\n\n')   
    f.write(h)
    f.close()
    
  #  print('出現次數='+str(gg))
    

    print('end')











