
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
  
    t=0
    for z in b.findAll("a"):
        if 'href' in z.attrs:
            t=t+1
            if 'title' in z.attrs:
                print(z.attrs['title'])
    return t
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

t=getw("https://zh.wikipedia.org/wiki/Wiki")

print("end*******************" , t)