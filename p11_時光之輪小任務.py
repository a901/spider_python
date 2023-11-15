


USER_SITE = "C:\ProgramData\Anaconda3\lib\site-packages" 

from bs4 import BeautifulSoup

import pymssql

from urllib.request import urlopen
from urllib.error import HTTPError

headers = {'user-agent': '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


#from BeautifulSoup import BeautifulSoup

#name = input('開始程式?')
#print(name)



for z in range(10,20):
    print(z)


global l
l=[]
global l2 #查詢類型
l2=[]
global y,y2
t=0
global task
t2=0

y=""
y2=""


def getw(a,k):
  
    try:
      html = urlopen (a)        
    except HTTPError as e :        
        return
  #  print("keep2") 
    b = BeautifulSoup(html.read())

    global y,y2
    ggg=""
    global task
    for z in b.findAll("h1"):
        ggg=z.text
        break
    for z in b.findAll("p"):
        
        if k in z.text:
            print(z.text)
           
                


#for z in range(20):
 #   t=getw("https://www.daocaorenshuwu.com/book/daliebu/"+(str)(1770576+0+z)+".html","麦特")

print("q1")

try:
    h = pymssql.connect(server='140.113.142.22:1433', user='a46911a149', password='0111', database='A01',charset='utf8')
except Exception as e:
    print(e)
    print("q2")
  


print("q2")
h2=h.cursor()

print("q3")      
h2.execute("SELECT * FROM b01")      
h3=h2.fetchall()

import re
text = 'asasasasffffffhhhhtyt'
text0 = text.replace('asf', '')
print(text0)


#清除爬蟲廣告語句

                
         
           

ti0="計算各角色始出場部數與末出場部數"        
m = [None] * 501
m2 = [None] * 501

n=26
for z in range(500):
    m[z]=-1
for z in range(500):
    m2[z]=-1
  
    
for z in h3:
    g=z[8]
    if z[23]==None:
        continue
    if z[23]>0 and m[g]==-1:
        m[g]=23
    if z[23]>0 :
        m2[g]=23
    if z[5]>0 and m[g]==-1:
        m[g]=5
    if z[5]>0 :
        m2[g]=5
    for i in range(10,23):
        if (z[i]>0 and m[g]==-1):
            m[g]=i
        if z[i]>0:
            m2[g]=i
 
print("iui")



title1="在擷取出場段落去除廣告文字"


g=""
r=""
ll=("daoＣaorenshuwu.ＣＯＭ","www.daocaorenshuwu.com","ＤaoＣaoＲenshuwu.ＣＯＭ",
    "歡迎到稻草人書屋看書","稻草人書屋免費下載TXT電子書 ",
    "daocaoＲenshuwu.Ｃom ","daocaoＲenshuwu.com","daocaorenshuwu.com","本文來自稻草人書屋"
    ,"daocaorenshuwu.ＣＯm ","copyright 稻草人書屋","daoＣaorenshuwu.com","daocaoＲenshuwu.coＭ"
    ,"Ｄaocaorenshuwu.com",'稻草人書屋',"內容來自"
    
    )

q=1
if q==1:
    print("start")
    for z in h3:
        for i in ll:
    
            g=(str)(z[27])
            r=i
            if r in g:
                print(z[0])
                print(g)
                print()
                g = g.replace(r, '')
                print(g)
                h2.execute("UPDATE b01  SET s0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))            
                h.commit()    
   
            g=(str)(z[28])
            if r in g:
                print(z[0])
                print(g)
                print()
                g = g.replace(r, '')
                print(g)
                h2.execute("UPDATE b01  SET e0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))            
                h.commit()
                
   
r=("","世界之眼","大狩獵","真龍轉生","闇影漸起",
					"天空之火","混沌之王","劍之王冠","匕之道",
					"寒冬之心","光影歧路","迷夢之刃","末日風暴",
					"闇夜之塔","光明回憶")


q=0
l=0

title2="在出場段落來源章節start end0 加入部名"

p=0
q=1
if q==1:
    for z in h3:
    
        
        print(z[0])
        l=m[z[8]]
        if l==23:
            l=0
        elif l==5:
            l=1
        else:
            l=l-8
         
        g=0
        if z[24]!=None and ("第" not in z[24] or "部" not in z[24]):
            
            g="第"+str(l)+"部"+r[l]+", "+z[24]
            print(g)
            h2.execute("UPDATE b01  SET start=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))            
            h.commit()
            
        l=m2[z[8]]
        if l==23:
            l=0
        elif l==5:
            l=1
        else:
            l=l-8
        if z[25]!=None and ("第" not in z[24] or "部" not in z[25]):
            g="第"+str(l)+"部"+r[l]+", "+z[25]
            print(g)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))            
            h.commit()
                
      
     
title3="轉簡體版用語為繁體版"
g=""
r=""
l1=["至上力","考索恩","芮娜","纔"
    
    ]
l2=["無極力","考松","李娜","才"
    
    ]

q=1
if q==1:
    print("start")
    for z in h3:
        for i in range(4):
    
            g=(str)(z[27])
            r=l1[i]
            if r in g:
                print(z[0])
                print(g)
                print()
                g = g.replace(r, l2[i])
                print(g)
            #    h2.execute("UPDATE b01  SET s0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))            
                h.commit()    
   
            g=(str)(z[28])
            if r in g:
                print(z[0])
                print(g)
                print()
                g = g.replace(r, l2[i])
                print(g)
             #   h2.execute("UPDATE b01  SET e0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))            
                h.commit()


title0="計算各角色總出場次數"

q=1
if q==1:
    for z in h3:
    
        g=0
        if z[23]!=None:
            g+=(int)(z[23])
        if z[5]!=None:
            g+=(int)(z[5])
                
        for i in range(10,23):
            if z[i]!=None:
                g+=z[i]
        print(z[0]+" "+(str)(g))
        h2.execute("UPDATE b01  SET [all]="+(str)(g)+" WHERE 編號="+(str)(z[8]) )            
        h.commit()





        
import opencc
cc = opencc.OpenCC('s2t')

#for z in h3:
 #   g=(str)(z[27])
  #  g=cc.convert(g)
   # h2.execute("UPDATE b01  SET s0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))   


            
h2.close()
h.close()
print("q5")

		

print("end***" , l)