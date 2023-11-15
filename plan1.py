
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
import sys
import pprint
pprint.pprint(sys.path)
for z in range(10):
    print(z)

t=0

def getw(a,m):
    if m>5:
        return m
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
  
    t=0
    for z in b.findAll("a"):
        if 'href' in z.attrs and 'title' in z.attrs:
            t=t+1
            if t>22 :
                print(z.attrs['title']," ",z.attrs['href'])
                t=getw("https://zh.wikipedia.org"+z.attrs['href'],m+1)
                break
            
            
    return t
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

t=getw("https://zh.wikipedia.org/wiki/Wiki",0)

print("end*******************" , t)