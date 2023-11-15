

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup

for z in range(10):
    print(z)


global l
l=[]
global l2
l2=[]
global t
t=0
global t2
t2=0

def getw(a,m,ti):
    global t,t2,l,l2
    if m>4:
        return 
    try:
     #   print("keep0_Anaconda " )
        print(str(m))
        html = urlopen (a)
        
    except HTTPError as e :   
        print("*\n*\n*\n")
        print("wrong")
        print(e)
        print("*\n*\n*\n")
        return
  #  print("keep2") 
    b = BeautifulSoup(html.read())
#    print("*\n*\n*\n")
   
    u0="https://zh.wikipedia.org"
    
    
    
    #for z in b.findAll("p"):
       # if '洪武' in z.text:
     #  print(z.text)
               # t=getw("https://zh.wikipedia.org"+z.attrs['href'],m+1)
        
    gg=0  
    print("start:")
    for z in b.findAll("a"):
        if 'href' in z.attrs :
            if 'accesskey' in z.attrs and 'h' in z.attrs['accesskey']:
                gettime(u0+z.attrs['href'],ti,m)
            if z.attrs['href'].startswith('/') and 'title' in z.attrs:
                gg=0
                for i in l:
                    if i==(u0+z.attrs['href']):
                        gg=1
                        break
                
                if gg==1:
                #    print("重複"+z.attrs['title'])
                    continue
                    
                t=t+1
                l.append(u0+z.attrs['href'])
               # print(z.attrs['title']," ",z.attrs['href'])
                if t%10==9:
                    #print(z.text)
                    getw("https://zh.wikipedia.org"+z.attrs['href'],m+1,z.attrs['title'])
            else:
                t2=t2+1
                l2.append(z.attrs['href'])
 #   print("start:")
    
    #for z in l2:
      #  print(z)
               # t=getw("https://zh.wikipedia.org"+z.attrs['href'],m+1)
          
            
    return t2

def gettime(a,g,m):
    print("gettime")
    try:
        print("gettime")
        html = urlopen (a)
        
    except HTTPError as e :   
        print("*\n*\n*\n")
        print("wrong")
        print(e)
        print("*\n*\n*\n")
        return
    b = BeautifulSoup(html.read())
    for z in b.findAll("a"):
        if 'class' in  z.attrs and 'mw-changeslist-date' in z.attrs['class'] :
              print(g+" "+z.text+" "+str(m))
              break
    
    return
            
    
    
    
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

t=getw("https://zh.wikipedia.org/wiki/%E5%9B%BD%E5%AD%90%E7%9B%91",0,"國子監")

print("end*******************" , t)