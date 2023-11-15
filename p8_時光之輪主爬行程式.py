

# 爬行時光之輪所有角色在所有部數出現之次數


USER_SITE = "C:\ProgramData\Anaconda3\lib\site-packages" 

from bs4 import BeautifulSoup

import pymssql

from urllib.request import urlopen
from urllib.error import HTTPError

headers = {'user-agent': '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


#from BeautifulSoup import BeautifulSoup

for z in range(10):
    print(z)

import opencc
cc = opencc.OpenCC('t2s')

global l
l=[]
global l2
l2=[]
global t
t=0
global t2
t2=0

def getw(a):
  
    

    k=""
    k2=""
    try:
      html = urlopen (a)        
    except HTTPError as e :        
        return -1
   
    global l,n
    b = BeautifulSoup(html.read())

    for z in h3: #
        l=0
        if z[8]>zn or z[8] in z2:   
            k=z[9]
            if z[1]!=None and z[1]!='' and z[6]>=20 and z[6]<30:
                k2=z[1]
            else:
                k2="jf鼯ruo"
                
            k2=cc.convert(k2)
          #  print(k2)
            for i in b.findAll("p"):     
                if  k in i.text   : #or "米海峨" in i.text   and "马吉尔" not in i.text and "吉尔丹" not in i.text 
                    l=l+1        
                    if l<6 or (l%10==1 ):
                        print("keep "+a) 
                        print(i.text)
                        print("\n\n")            
            n[z[8]]+=l
            
    return 0
        


    
def inquire(s,w,y):
    global l
    
    g=0
    for z in h3: #
        l=0
        if z[8]>zn or z[8] in z2:   
            g=1
            break
    if g==0:
        return
    
    l=0
    g=0
    for z in range(w):
        #print("keep"+str(z))
        g=getw(y+(str)(s+z)+".html")
        if g==-1:
            continue
        
        for j in range(2,40):
            g=getw(y+(str)(s+z)+"_"+(str)(j)+".html")
            if g==-1:
                break
        

      
  


  
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
global h3
h3=h2.fetchall()



    #inquire13(z[9])
    #l+=z[21]
    #print(l)
   # print(z[21])
  #  h2.execute("UPDATE b01  SET [13]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )  
  #  h.commit()
  
 
    
#ggg=input("input")



global n
n=[0] *600

for i in range(600):
    n[i]=0    
 

zn=418
z2=[176,208,91,81,139,290,1000,2000]
#z2=(158,165,1000,2000)

        

        

q=0
if q==0:
    print("第二部:")#爬所有角色第二部之資料   z[10]
    inquire(1770576,50,"https://www.daocaorenshuwu.com/book/daliebu/")#50
    for z in h3: 
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [02]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0   
     
 
q=0
if q==0:
    print("第三部:")#爬所有角色第三部之資料   z[11]
    inquire(1770629,55,"https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/")
    
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [03]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0      
       

q=0 
if q==0:
    print("第四部:")#爬所有角色第三部之資料   z[12]
    inquire(1770688,58,"https://www.daocaorenshuwu.com/book/anyingjianqi/")
    
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [04]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0      
  
  
q=0 
if q==0:
    print("第五部:")#爬所有角色第5部之資料   z[13]
    inquire(1770749,57,"https://www.daocaorenshuwu.com/book/tiankongzhihuo/")
   
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [05]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0  


q=0 
if q==0:
    print("第六部:")#爬所有角色第5部之資料   z[14]
    inquire(1770809,58,"https://www.daocaorenshuwu.com/book/hunchunzhiwang/")
   
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [06]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0  


q=0 
if q==0:
    print("第七部:")#爬所有角色第5部之資料   z[15]
    inquire(1770871,42,"https://www.daocaorenshuwu.com/book/jianzhiwangguan/")
   
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [07]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0  

q=0 
if q==0:
    print("第八部:")#爬所有角色第5部之資料   z[16]
    inquire(1770917,32,"https://www.daocaorenshuwu.com/book/bishouzhilu/")
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [08]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0 
    

q=0 
if q==0:
    print("第九部:")#爬所有角色第5部之資料   z[17]
    inquire(1770951,37,"https://www.daocaorenshuwu.com/book/handongzhixin/")
    
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [09]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0 
         
    
q=0 
if q==0:
    print("第十部:")#爬所有角色第5部之資料   z[18]
    inquire(1770992,32,"https://www.daocaorenshuwu.com/book/guangyingqilu/")
  
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [10]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0            
      
q=0 
if q==0:
    print("第十一部:")#爬所有角色第5部之資料   z[19]
    inquire(1771028,39,"https://www.daocaorenshuwu.com/book/mimengzhiren/")
   
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [11]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0  
           
q=0 
if q==0:
    print("第十二部:")#爬所有角色第5部之資料   z[20]
    inquire(1771070,52,"https://www.daocaorenshuwu.com/book/morifengbao/")
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [12]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0             


           
q=0 
if q==0:
    print("第十三部:")#爬所有角色第5部之資料   z[21]
    inquire(1771128,60,"https://www.daocaorenshuwu.com/book/wuyegaota/")
   
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [13]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0     


q=0 
if q==0:
    print("第十四部:")#爬所有角色第5部之資料   z[22]
    inquire(1771191,53,"https://www.daocaorenshuwu.com/book/guangminghuiyi/")
 
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [14]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0     
    


q=0 
if q==0:
    print("第一部:")#爬所有角色第5部之資料   z[5]
    inquire(1770521,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_shang/")
    inquire(1770548,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_xia/")
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [01]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0     

q=0 
if q==0:
    print("前傳:")#爬所有角色第5部之資料   z[23]
    inquire(1770492,27,"https://www.daocaorenshuwu.com/book/shiguangzhilun/")
    for z in h3:
        if z[8]>zn or z[8] in z2:  
            print(z[0]+" "+str(n[z[8]]))
            h2.execute("UPDATE b01  SET [00]="+(str)(n[z[8]])+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
            n[z[8]]=0
for i in range(200):
    n[i]=0  
    
    
            
h2.close()
h.close()
print("q5")

		


print("end*******************" , l)