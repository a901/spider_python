

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
  #  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
  #  req = urllib.request.Request(url=chaper_url, headers=headers)

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
  
    t=0
    for z in b.findAll("a"):
        if 'span' in z.attrs :
            t=t+1
            print(z.attrs['class']," ",z.text)
               
            
            
            
    return t
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

t=getw("https://www.pttweb.cc/bbs/Boy-Girl/M.1574914157.A.893",0)

print("end*******************" , t)