


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
        return -1
  #  print("keep2") 
    b = BeautifulSoup(html.read())

    global y,y2
    ggg=""
    global task
    for z in b.findAll("h1"):
        ggg=z.text
        break
    for z in b.findAll("p") :
        
        if  k in z.text  and "爱拉妮" not in z.text and "爱拉瑟勒" not in z.text :
            print(z.text)
            if task==1:
                task=0
                y=z.text
                y2=ggg
                break
            if task==2:
                y=z.text
                y2=ggg
    return 0
                
         
           
        


    
def inquire(k,s,w,yy):
   
    global y,y2
    global task
    g=0
   
    for z in range(w):
        if task==0:
            break;
        #print("keep"+str(z))
        g=getw(yy+(str)(s+z)+".html",k)
        if g==-1:
            continue
        if task==0:
            break
        
        for j in range(2,40):
            if task==0:
                break
            g=getw(yy+(str)(s+z)+"_"+(str)(j)+".html",k)
            if g==-1:
                break
    
   
    
  
def inquire14(k):#14
   
    
    s="https://www.daocaorenshuwu.com/book/guangminghuiyi/1771228"
    
    for i in range(5,35): 
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
   
    s="https://www.daocaorenshuwu.com/book/guangminghuiyi/1771191"  
    for i in range(5,35):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
     
   
    

    
def inquire6(k):#6
    global l
    s="https://www.daocaorenshuwu.com/book/hunchunzhiwang/1770809"
    
   
    for i in range(5,36):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
    
      
    print(k+" "+(str)(l)) 
    
def inquire3(k):#3
    global l
    s="https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/1770683"   
    for i in range(5,6):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)       
    print(k+" "+(str)(l)) 
    

def inquire4(k):#4
    global l
    s="https://www.daocaorenshuwu.com/book/anyingjianqi/1770688"  
    for i in range(5,6):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
    s="https://www.daocaorenshuwu.com/book/anyingjianqi/1770689"  
    for i in range(5,6):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
    print(k+" "+(str)(l)) 

def inquire5(k):#5
    global l
    s="https://www.daocaorenshuwu.com/book/tiankongzhihuo/1770750"  
    for i in range(5,6):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l)) 
    
def inquire7(k):#7
    global l
    s="https://www.daocaorenshuwu.com/book/jianzhiwangguan/1770871"  
    for i in range(5,7):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l)) 
    
def inquire9(k):#9
    global l
    s="https://www.daocaorenshuwu.com/book/handongzhixin/1770951"  
    for i in range(5,34):   
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l))   
    
def inquire10(k):#10
    global l
    s="https://www.daocaorenshuwu.com/book/guangyingqilu/1770992"  
    for i in range(5,37):   
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l))   

def inquire11(k):#11
    global l
    s="https://www.daocaorenshuwu.com/book/mimengzhiren/1771028"  
    for i in range(5,16):   
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
    s="https://www.daocaorenshuwu.com/book/mimengzhiren/1771052"  
    for i in range(5,6):    
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l))  
    
def inquire13(k):#13
    global l
    s="https://www.daocaorenshuwu.com/book/wuyegaota/1771128"  
    for i in range(5,6): 
        if task==0:
            break
        getw(s+"_"+(str)(i)+".html",k)
  
  
    print(k+" "+(str)(l))    
      
 
    
    
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")
l=0
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
h2.execute("SELECT * FROM b01 ORDER BY 編號  ASC")      
h3=h2.fetchall()




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
        print(z[i])
        if z[i]==None:
            continue
        if (z[i]>0 and m[g]==-1):
            m[g]=i
        if z[i]>0:
            m2[g]=i
            
            
import opencc
cc = opencc.OpenCC('s2t')

#for z in h3:
 #   g=(str)(z[27])
  #  g=cc.convert(g)
   # h2.execute("UPDATE b01  SET s0=N'"+(str)(g)+"' WHERE 編號="+(str)(z[8]))   

#z2=(133,1000,2000)



zn=418
z2=[176,208,91,81,139,290,1000,2000]
q=0
task=0


q=0
if q==0:
    print("第二部:")
    for z in h3: #爬所有角色第二部之資料   z[10]

        if ((z[8]>zn or z[8] in z2) and m[z[8]]==10):  
            y=""
            y2=""
            print(z[0]+" t1")
            task=1
            inquire(z[9],1770576,50,"https://www.daocaorenshuwu.com/book/daliebu/")#50
            print(z[0]+" "+y2)
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8]))  
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))            
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==10):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
            inquire(z[9],1770576,50,"https://www.daocaorenshuwu.com/book/daliebu/")#50
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()



q=0
task=0

if q==0 :
    print("第三部:")
    for z in h3: #爬所有角色第三部之資料   z[11]
        
        if(z[8]>zn or z[8] in z2) and m[z[8]]==11: 
            print(z[0]+" t1")
            y=""
            y2=""
            task=1
            inquire(z[9],1770629,55,"https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/")
            #inquire3(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==11):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
          #  inquire3(z[9])
            inquire(z[9],1770629,55,"https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()

q=0
task=0
if q==0:
    print("第四部:")
    for z in h3: #爬所有角色第四部之資料   z[12]
        
         
        if (z[8]>zn or z[8] in z2) and m[z[8]]==12: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1770688,58,"https://www.daocaorenshuwu.com/book/anyingjianqi/")
          #  inquire4(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==12):   
            y=""
            y2=""
            print(z[0]+" t2")
            task=2
           # inquire4(z[9])
            inquire(z[9],1770688,58,"https://www.daocaorenshuwu.com/book/anyingjianqi/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
        


q=0
if q==0:
    print("第五部:")
    for z in h3: #爬所有角色第五部之資料   z[13]
        
        
        
        
        if (z[8]>zn or z[8] in z2) and m[z[8]]==13: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1770749,57,"https://www.daocaorenshuwu.com/book/tiankongzhihuo/")
          #  inquire5(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==13):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
          #  inquire5(z[9])
            inquire(z[9],1770749,57,"https://www.daocaorenshuwu.com/book/tiankongzhihuo/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()

q=0

if q==0:
    print("第六部:")
    for z in h3: #爬所有角色第6部之資料   z[14]
        if (z[8]>zn or z[8] in z2) and m[z[8]]==14: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
          #  inquire6(z[9])
            inquire(z[9],1770809,58,"https://www.daocaorenshuwu.com/book/hunchunzhiwang/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==14):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
          #  inquire6(z[9])
            inquire(z[9],1770809,58,"https://www.daocaorenshuwu.com/book/hunchunzhiwang/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
       
      

q=0
if q==0:
    print("第七部:")
    for z in h3: #爬所有角色第7部之資料   z[15]
      
        if (z[8]>zn or z[8] in z2) and m[z[8]]==15: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1770871,42,"https://www.daocaorenshuwu.com/book/jianzhiwangguan/")
         #   inquire7(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==15):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
        #    inquire7(z[9])
            inquire(z[9],1770871,42,"https://www.daocaorenshuwu.com/book/jianzhiwangguan/")
           
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
      
      

q=0
if q==0:
    print("第八部:")
    for z in h3: #爬所有角色第8部之資料   z[16]
        if (z[8]>zn or z[8] in z2) and m[z[8]]==16: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1770917,32,"https://www.daocaorenshuwu.com/book/bishouzhilu/")
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==16):   
            y=""
            y2=""
            print(z[0]+" t2")
            task=2
            inquire(z[9],1770917,32,"https://www.daocaorenshuwu.com/book/bishouzhilu/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
        
       

q=0
if q==0:
    print("第九部:")
    for z in h3: #爬所有角色第8部之資料   z[17]
        if (z[8]>zn or z[8] in z2) and m[z[8]]==17: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1770951,37,"https://www.daocaorenshuwu.com/book/handongzhixin/")
        #    inquire9(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==17):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
         #   inquire9(z[9])
            inquire(z[9],1770951,37,"https://www.daocaorenshuwu.com/book/handongzhixin/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
        
    
       
    

q=0
if q==0:
    print("第十部:")
    for z in h3: #爬所有角色第8部之資料   z[18]
        if (z[8]>zn or z[8] in z2) and m[z[8]]==18: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1770992,32,"https://www.daocaorenshuwu.com/book/guangyingqilu/")
          #  inquire10(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==18):   
            y=""
            y2=""
            print(z[0]+" t2")
            task=2
         #   inquire10(z[9])
            inquire(z[9],1770992,32,"https://www.daocaorenshuwu.com/book/guangyingqilu/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
      
             
            
q=0
if q==0:
    print("第十一部:")
    for z in h3: #爬所有角色第8部之資料   z[19]   
         
        if (z[8]>zn or z[8] in z2) and m[z[8]]==19: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1771028,39,"https://www.daocaorenshuwu.com/book/mimengzhiren/")
        #    inquire11(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==19):   
            y=""
            y2=""
            print(z[0]+" t2")
            task=2
          #  inquire11(z[9])
            inquire(z[9],1771028,39,"https://www.daocaorenshuwu.com/book/mimengzhiren/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
      
       
               
                     

q=0
if q==0:
    print("第十二部:")
    for z in h3: #爬所有角色第8部之資料   z[20] 
        
        
        
        if (z[8]>zn or z[8] in z2) and m[z[8]]==20: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1771070,52,"https://www.daocaorenshuwu.com/book/morifengbao/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==20):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
           
            inquire(z[9],1771070,52,"https://www.daocaorenshuwu.com/book/morifengbao/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
            
                            
q=0
if q==0:
    print("第十三部:")
    for z in h3: #爬所有角色第13部之資料   z[21]  
        
           
        if (z[8]>zn or z[8] in z2) and m[z[8]]==21: 
            print(z[0]+" t1")
            task=1
            y=""
            y2=""
            inquire(z[9],1771128,60,"https://www.daocaorenshuwu.com/book/wuyegaota/")
         #   inquire13(z[9])
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==21):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
          #  inquire13(z[9])
            inquire(z[9],1771128,60,"https://www.daocaorenshuwu.com/book/wuyegaota/")
            
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
            

 
q=0
if q==0:
    print("第十四部:")
    for z in h3: #爬所有角色第14部之資料   z[22]
        
        if (z[8]>zn or z[8] in z2) and m[z[8]]==22: 
            print(z[0]+" t1")
            task=1
          #  inquire14(z[9])
            inquire(z[9],1771191,53,"https://www.daocaorenshuwu.com/book/guangminghuiyi/")
            y=""
            y2=""
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==22):   
            y="" 
            y2=""
            print(z[0]+" t2")
            task=2
          #  inquire14(z[9])
            inquire(z[9],1771191,53,"https://www.daocaorenshuwu.com/book/guangminghuiyi/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
       
       

q=0
if q==0:
    print("第一部:")
    for z in h3: #爬所有角色第1部之資料   z[5]   
        if (z[8]>zn or z[8] in z2) and m[z[8]]==5: 
            y=""
            y2=""
            print(z[0]+" t1")
            task=1
            inquire(z[9],1770521,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_shang/")#
            inquire(z[9],1770548,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_xia/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==5):   
            y=""
            y2=""
            print(z[0]+" t2")
            task=2
            inquire(z[9],1770521,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_shang/")
            inquire(z[9],1770548,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_xia/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
       

q=0
if q==0:
    
    for z in h3: #爬所有角色第1部之資料   z[23]   
       
        if (z[8]>zn or z[8] in z2) and m[z[8]]==23: 
            y=""
            print(z[0]+" t1")
            task=1
            inquire(z[9],1770492,27,"https://www.daocaorenshuwu.com/book/shiguangzhilun/")
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET start=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET s0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]))             
            h.commit()
        
        if ((z[8]>zn or z[8] in z2) and m2[z[8]]==23):   
            y=""
             
            print(z[0]+" t2")
            task=2
            inquire(z[9],1770492,27,"https://www.daocaorenshuwu.com/book/shiguangzhilun/")
           
            print(z[0]+" ")
            print(y)
            y=cc.convert(y)
            y2=cc.convert(y2)
            h2.execute("UPDATE b01  SET end0=N'"+(str)(y2)+"' WHERE 編號="+(str)(z[8])) 
           
            h2.execute("UPDATE b01  SET e0=N'"+(str)(y)+"' WHERE 編號="+(str)(z[8]) )            
            h.commit()
       
     



            
h2.close()
h.close()
print("q5")

		
for z in range(1):
    t=getw("https://www.daocaorenshuwu.com/book/daliebu/1770576/"+(str)(780+z)+".html",0)

print("end*******************" , l)