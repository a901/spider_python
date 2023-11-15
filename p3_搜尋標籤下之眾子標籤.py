
#Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup

for z in range(10):
    print(z)

t=0

def getw(a):
    try:
        print("keep0")
        html = urlopen (a)
        
    except HTTPError as e :   
        print("*\n*\n*\n")
        print("wrong")
        print(e)
        print("*\n*\n*\n")
        return
    print("keep2") 
    b = BeautifulSoup(html.read())
    print("*\n*\n*\n")
   # for z in b.find("header",{"class":"boxTitle"}).children:
    #    print(z)
    #descendants
    t=0
    for z in b.find("div",{"class":"menulist"}).children:
        print(z)
        t=t+1
    return t
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

t=getw("http://news.ltn.com.tw/news/politics/paper/19217")

print("end*******************" , t)