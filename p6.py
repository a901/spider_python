
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import tkinter as tk

#from BeautifulSoup import BeautifulSoup

for z in range(10):
    print(z)

t=0
g=0

l=0

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
    g=0
    global l
    l=0
    
    for z in b.findAll("a" , "td"):
        if 'href' in z.attrs:
            g=g+1
            print("href")
        if 'rowspan' in z.attrs and g>0:
            t=t+1
            l=l+g
            g=0
            #print(z.attrs['title']," ",z.attrs['href'])
   
            #print(z.attrs['title']," ",z.attrs['href'])
       
            
    return g
    
t=getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/%E4%BA%A4%E5%8F%89.html",0)

#t=getw("https://zh.wikipedia.org/wiki/Wiki",0)


window = tk.Tk()
window.title('my window')
window.geometry('400x300')

b1  =  tk.Label(window,text  = ' Hello Tkinter ' ,font=('Arial', 12)  ) 
    # 標籤長寬
b1.pack()    # 固定窗口位置

# window.mainloop()


# 這裏是窗口的內容



print("end*******************" , t)
print("end*******************" , l)