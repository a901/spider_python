


USER_SITE = "C:\ProgramData\Anaconda3\lib\site-packages" 

from bs4 import BeautifulSoup

import pymssql

from urllib.request import urlopen
from urllib.error import HTTPError

headers = {'user-agent': '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


#from BeautifulSoup import BeautifulSoup

#name = input('開始程式?')
#print(name)



for z in range(10):
    print(z)


global l
l=[]
global l2 #查詢類型
l2=[]
global t
t=0
global t2
t2=0

def getw(a,k):
  
    global l,l2

    try:
      html = urlopen (a)        
    except HTTPError as e :        
        return
  #  print("keep2") 
    b = BeautifulSoup(html.read())

    for z in b.findAll("p"):
        
        if k in z.text :
            l=l+1
            if l2==1 and l>10:
                break
           
            if ((l2>1 ) or (l2==1 and l<10)) :
                print(z.text)
                print("\n\n")
        


    
def inquire(k,s,w,y):
    global l,l2
    
    l=0
    for z in range(w):
        
        getw(y+(str)(s+z)+".html",k)
        getw(y+(str)(s+z)+"_2.html",k)
        getw(y+(str)(s+z)+"_3.html",k)
        getw(y+(str)(s+z)+"_4.html",k)
        
        if l2==1 and l>10:
                break
      
    print(k+" "+(str)(l))
    if l==3:      
        name = input('繼續執行程式?')
        print(name)
    
    
def inquire14(k):#14
    global l
    s="https://www.daocaorenshuwu.com/book/guangminghuiyi/1771228"
    
    for i in range(5,35):    
        getw(s+"_"+(str)(i)+".html",k)
   
    s="https://www.daocaorenshuwu.com/book/guangminghuiyi/1771191"  
    for i in range(5,35):    
        getw(s+"_"+(str)(i)+".html",k)
     
    print(k+" "+(str)(l)) 
    

    
def inquire6(k):#6
    global l
    s="https://www.daocaorenshuwu.com/book/hunchunzhiwang/1770809"
    
   
    for i in range(5,36):    
        getw(s+"_"+(str)(i)+".html",k)
    
      
    print(k+" "+(str)(l)) 
    
def inquire3(k):#3
    global l
    s="https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/1770683"   
    for i in range(5,6):    
        getw(s+"_"+(str)(i)+".html",k)       
    print(k+" "+(str)(l)) 
    

def inquire4(k):#4
    global l
    s="https://www.daocaorenshuwu.com/book/anyingjianqi/1770688"  
    for i in range(5,6):    
        getw(s+"_"+(str)(i)+".html",k)
    s="https://www.daocaorenshuwu.com/book/anyingjianqi/1770689"  
    for i in range(5,6):    
        getw(s+"_"+(str)(i)+".html",k)
    print(k+" "+(str)(l)) 

def inquire5(k):#5
    global l
    s="https://www.daocaorenshuwu.com/book/tiankongzhihuo/1770750"  
    for i in range(5,6):    
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l)) 
    
def inquire7(k):#7
    global l
    s="https://www.daocaorenshuwu.com/book/jianzhiwangguan/1770871"  
    for i in range(5,7):    
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l)) 
    
def inquire9(k):#9
    global l
    s="https://www.daocaorenshuwu.com/book/handongzhixin/1770951"  
    for i in range(5,34):    
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l))   
    
def inquire10(k):#10
    global l
    s="https://www.daocaorenshuwu.com/book/guangyingqilu/1770992"  
    for i in range(5,37):    
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l))   

def inquire11(k):#11
    global l
    s="https://www.daocaorenshuwu.com/book/mimengzhiren/1771028"  
    for i in range(5,16):    
        getw(s+"_"+(str)(i)+".html",k)
    s="https://www.daocaorenshuwu.com/book/mimengzhiren/1771052"  
    for i in range(5,6):    
        getw(s+"_"+(str)(i)+".html",k)
  
    print(k+" "+(str)(l))  
    
def inquire13(k):#13
    global l
    s="https://www.daocaorenshuwu.com/book/wuyegaota/1771128"  
    for i in range(5,6):    
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



k0=102   # 查詢角色之永久編號
k2=(13,100,200,400) #(1,2,3,4,5,6,7,8,9,10,11,12,13,14,0)  查詢小說部數
l2=2 # 類型 查初次出場1 查結局2 查大量章節內文_會暫停等待3


zn=3330
z2=[1000,2000]
import opencc
c2 = opencc.OpenCC('t2s')
#z2=(158,165,1000,2000)
for z in h3: 
    if z[6]>=20 and z[6]<30:
        g=int(z[8])
        print(z[1])
        kk=z[1]
        kk=c2.convert(kk)
        print(kk)
        z2.append(g)
print("test")       
for i in z2:
    print(i)
    
      
        
        
q=0
if 2 in k2:
    print("第二部:")
    for z in h3: #爬所有角色第二部之資料   z[10]
        
        if z[8]==k0:  
            print(z[0])
            inquire(z[9],1770576,50,"https://www.daocaorenshuwu.com/book/daliebu/")#50
           
            print(z[0]+" "+(str)(l))
           # h2.execute("UPDATE b01  SET [02]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
        
q=0
if 3 in k2:
    print("第三部:")
    for z in h3: #爬所有角色第三部之資料   z[11]
        
        if z[8]==k0:  
            print(z[0])
            inquire(z[9],1770629,55,"https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/")
            inquire3(z[9])
            print(z[0]+" "+(str)(l))
          #  h2.execute("UPDATE b01  SET [03]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()

q=0
if 4 in k2:
    print("第四部:")
    for z in h3: #爬所有角色第四部之資料   z[12]
        
        if  z[8]==k0:
            print(z[0])
            inquire(z[9],1770688,58,"https://www.daocaorenshuwu.com/book/anyingjianqi/")
            inquire4(z[9])
            print(z[0]+" "+(str)(l))
           # h2.execute("UPDATE b01  SET [04]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()    

q=0
if 5 in k2:
    print("第五部:")
    for z in h3: #爬所有角色第五部之資料   z[13]
     
        
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1770749,57,"https://www.daocaorenshuwu.com/book/tiankongzhihuo/")
            inquire5(z[9])
            print(z[0]+" "+(str)(l))
          #  h2.execute("UPDATE b01  SET [05]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()   

q=0
if 6 in k2:
    print("第六部:")
    for z in h3: #爬所有角色第6部之資料   z[14]
       
        
        if z[8]==k0:  
            print(z[0])
            inquire(z[9],1770809,58,"https://www.daocaorenshuwu.com/book/hunchunzhiwang/")
            inquire6(z[9])
            print(z[0]+" "+(str)(l))
          #  h2.execute("UPDATE b01  SET [06]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if 7 in k2:
    print("第七部:")
    for z in h3: #爬所有角色第7部之資料   z[15]
        
        
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1770871,42,"https://www.daocaorenshuwu.com/book/jianzhiwangguan/")
            inquire7(z[9])
            print(z[0]+" "+(str)(l))
           # h2.execute("UPDATE b01  SET [07]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if 8 in k2:
    print("第八部:")
    for z in h3: #爬所有角色第8部之資料   z[16]
    
        
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1770917,32,"https://www.daocaorenshuwu.com/book/bishouzhilu/")
         
            print(z[0]+" "+(str)(l))
           # h2.execute("UPDATE b01  SET [08]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if 9 in k2:
    print("第九部:")
    for z in h3: #爬所有角色第8部之資料   z[17]
    
       
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1770951,37,"https://www.daocaorenshuwu.com/book/handongzhixin/")
            inquire9(z[9])
            print(z[0]+" "+(str)(l))
        #    h2.execute("UPDATE b01  SET [09]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if 10 in k2:
    print("第十部:")
    for z in h3: #爬所有角色第8部之資料   z[18]
      
       
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1770992,32,"https://www.daocaorenshuwu.com/book/guangyingqilu/")
            inquire10(z[9])
            print(z[0]+" "+(str)(l))
          #  h2.execute("UPDATE b01  SET [10]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()          
            
q=0
if 11 in k2:
    print("第十一部:")
    for z in h3: #爬所有角色第8部之資料   z[19]   
     
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1771028,39,"https://www.daocaorenshuwu.com/book/mimengzhiren/")
            inquire11(z[9])
            print(z[0]+" "+(str)(l))
         #   h2.execute("UPDATE b01  SET [11]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()          
                     

q=0
if 12 in k2:
    print("第十二部:")
    for z in h3: #爬所有角色第8部之資料   z[20]   
      
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1771070,52,"https://www.daocaorenshuwu.com/book/morifengbao/")
            
            print(z[0]+" "+(str)(l))
          #  h2.execute("UPDATE b01  SET [12]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()          
                            
q=0
if 13 in k2:
    print("第十三部:")
    for z in h3: #爬所有角色第13部之資料   z[21]   
       
        if z[8]==k0:  
            print(z[0])
            inquire(z[9],1771128,60,"https://www.daocaorenshuwu.com/book/wuyegaota/")
            inquire13(z[9])
            print(z[0]+" "+(str)(l))
           # h2.execute("UPDATE b01  SET [13]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()   
q=0
if 14 in k2:
    print("第十四部:")
    for z in h3: #爬所有角色第14部之資料   z[22]   
        
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1771191,53,"https://www.daocaorenshuwu.com/book/guangminghuiyi/")
            inquire14(z[9])
            print(z[0]+" "+(str)(l))
        #    h2.execute("UPDATE b01  SET [14]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()   

q=0
if 1 in k2:
    print("第一部:")
    for z in h3: #爬所有角色第1部之資料   z[5]   
       
        if z[8]==k0: 
            print(z[0])
            inquire(z[9],1770521,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_shang/")
            print(z[0]+" "+(str)(l))
            gg=l
            inquire(z[9],1770548,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_xia/")
            gg+=l
            print(z[0]+" "+(str)(l)+" "+(str)(gg))
          #  h2.execute("UPDATE b01  SET [01]="+(str)(gg)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()  

q=0
if 0 in k2:
    print("前傳:")
    for z in h3: #爬所有角色第1部之資料   z[23]   
      
        if z[8]==k0:  
            print(z[0])
            inquire(z[9],1770492,27,"https://www.daocaorenshuwu.com/book/shiguangzhilun/")
            print(z[0]+" "+(str)(l))
           
          #  h2.execute("UPDATE b01  SET [00]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()  


            
h2.close()
h.close()
print("q5")

		
for z in range(1):
    t=getw("https://www.daocaorenshuwu.com/book/daliebu/1770576/"+(str)(780+z)+".html",0)

print("end*******************" , l)