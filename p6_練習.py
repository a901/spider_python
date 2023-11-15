

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup

for z in range(10):
    print(z)

t=0

def getw(a,m):
    if m>5:
        return m
    try:
        print("keep0_Anaconda")
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
    l=[]
    l2=[]
    t=0
    t2=0;
    u0="https://zh.wikipedia.org"
    
    
    for z in b.findAll("p"):
        if '洪武' in z.text:
            print(z.text)
               # t=getw("https://zh.wikipedia.org"+z.attrs['href'],m+1)
        
        
    print("start:")
    for z in b.findAll("a"):
        if 'href' in z.attrs :
            if z.attrs['href'].startswith('/'):
                t=t+1
                l.append(u0+z.attrs['href'])
               # print(z.attrs['title']," ",z.attrs['href'])
               # t=getw("https://zh.wikipedia.org"+z.attrs['href'],m+1)
            else:
                t2=t2+1
                l2.append(z.attrs['href'])
    print("start:")
    
    for z in l2:
        print(z)
               # t=getw("https://zh.wikipedia.org"+z.attrs['href'],m+1)
          
            
    return t2
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

t=getw("https://zh.wikipedia.org/wiki/%E5%9B%BD%E5%AD%90%E7%9B%91",0)

print("end*******************" , t)