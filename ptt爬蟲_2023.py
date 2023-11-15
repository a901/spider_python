# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:08:55 2023

@author: a4691
"""

import requests
import time
import re
from bs4 import BeautifulSoup
import csv

PTT_URL = 'https://www.ptt.cc'
API_KEY = '26266720e9aa08a4477f6ed04c1404ec'


def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html5lib')

    # 取得上一頁的連結
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []  # 儲存取得的文章資料
    authortotal=[]
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        if d.find('div', 'date').text.strip() == date:  # 發文日期正確
            # 取得推文數
            push_count = 0
            push_str = d.find('div', 'nrec').text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換字串為數字
                except ValueError:
                    # 若轉換失敗，可能是'爆'或 'X1', 'X2', ...
                    # 若不是, 不做任何事，push_count 保持為 0
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10

            # 取得文章連結及標題
            if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                href = d.find('a')['href']
                title = d.find('a').text
                author = d.find('div', 'author').text if d.find('div', 'author') else ''
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count,
                    'author': author
                })
                authortotal.append(author)
    return articles, prev_url,authortotal


def get_ip(dom):
    # e.g., ※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 27.52.6.175
    pattern = '來自: \d+\.\d+\.\d+\.\d+'
    match = re.search(pattern, dom)
    if match:
        return match.group(0).replace('來自: ', '')
    else:
        return None


def get_country(ip):
    if ip:
        url = 'http://api.ipstack.com/{}?access_key={}'.format(ip, API_KEY)
        data = requests.get(url).json()
        country_name = "cn" #data['country_name'] if data['country_name'] else None
        return country_name
    return None


def get_context(k): # 取得文章內容
    
    
  #  match = re.search('標題</span><span class="article-meta-value">(\Z|\S|\s|\n|.)*', k)
    
    arr = k.split('標題</span><span class="article-meta-value">')
    ar2= arr[1].split('<span class="f2">※ 發信站: 批踢踢實業坊(ptt.cc), 來自')
    return ar2[0]




if __name__ == '__main__':
    print('取得今日女版文章列表...')
    current_page = get_web_page(PTT_URL + '/bbs/WomenTalk/index.html')
    
    if current_page:
        articles = []  # 全部的今日文章
        author=[]
        countryT=[]
        title=[]
        today = time.strftime('%m/%d').lstrip('0')  # 今天日期, 去掉開頭的 '0' 以符合 PTT 網站格式
        current_articles, prev_url,authortotal = get_articles(current_page, today)  # 目前頁面的今日文章
        while current_articles:  # 若目前頁面有今日文章則加入 articles，並回到上一頁繼續尋找是否有今日文章
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url,authortotal = get_articles(current_page, today)
        print('共 %d 篇文章' % (len(articles)))

        # 已取得文章列表，開始進入各文章尋找發文者 IP
        print('取得前 100 篇文章 IP')
        country_to_count = dict()
        for article in articles[3:5]:
            print('查詢 IP:', article['title'])
            page = get_web_page(PTT_URL + article['href'])
            if page:
                ip = get_ip(page)
                country = get_country(ip)
                if country in country_to_count.keys():
                    country_to_count[country] += 1
                else:
                    country_to_count[country] = 1
            print("來自",country, end='')
            print("   ","作者是",article['author'])
            author.append(article['author'])
            title.append(article['title'])
            countryT.append(country)
            
            
            g=get_context(page )
            print(g)
            
            print("\n====\n")
        # 印出各國 IP 次數資訊
        print('各國 IP 分布')
        for k, v in country_to_count.items():
            print(k, v)