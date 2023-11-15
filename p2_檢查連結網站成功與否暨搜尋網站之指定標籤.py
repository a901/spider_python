
#Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup


def getw(a):
    try:
        
        html = urlopen (a)
        print("keep1")
    except HTTPError as e :   
        print("*\n*\n*\n")
        print("wrong")
        print(e)
        print("*\n*\n*\n")
        return
    print("keep2") 

    if html is None:
        print("*\n*\n*\n")
        print("no found")
        print("*\n*\n*\n")
        return
    else:
        b = BeautifulSoup(html.read())
        print("*\n*\n*\n")
        print(b.h1)
        print("*\n*\n*\n")
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

getw("http://news.ltn.com.tw/news/politics/paper/19217")
print("end*******************")