

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


global l
l=[]
global l2
l2=[]
global t
t=0
global t2
t2=0

def getw(a,k,k2):
  
    global l

    try:
      html = urlopen (a)        
    except HTTPError as e :        
        print("e")
        return -1
    print("keep2") 
    b = BeautifulSoup(html.read())
    print("keep3") 
    for z in b.findAll("p"):
        
        if k in z.text or k2 in z.text:
            l=l+1
           
            if l<10 or (l%5==1 and l<30):
                print(z.text)
                print("\n\n")
    return 0


    
def inquire(k,k2,s,w,y):
    global l
    
    l=0
    for z in range(w):
        g=getw(y+(str)(s+z)+".html",k,k2)
        
        
     
      
    print(k+" "+(str)(l)+" ##")



     
#getw("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")
l=0
#for z in range(20):
 #   t=getw("https://www.daocaorenshuwu.com/book/daliebu/"+(str)(1770576+0+z)+".html","麦特")

headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',#如某些網站（如p站）要檢查referer，就給他加上
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'#每個爬蟲必備的偽裝
}

print("q1")

try:
    h = pymssql.connect(server='140.113.142.22:1433', user='a46911a149', password='0111', database='A01',charset='utf8')
except Exception as e:
    print(e)
    print("q2")
  
# 

try:
    html = urlopen ("https://tapchipi.com/enchanted-inc/page-3-4298/")        
except HTTPError as e :        
    print("e")
   
print("keep20000") 
b = BeautifulSoup(html.read())
print("keep3") 
    
l=0
for z in b.findAll("p"):
    l=l+1
    print(z.text)
    print("\n\n")   

print("q2"+" "+str(l))
h2=h.cursor()

print("q3")      
h2.execute("SELECT * FROM b01 ORDER BY 編號  ASC")      
h3=h2.fetchall()



kk=460

q=0
if q==0:
    print("第二部:")
    for z in h3: #爬所有角色第二部之資料   z[10]
        #print(z[0])
        if kk==z[8]:   
            print(z[0]+" "+(str)(l)+" #")
            inquire("min","Min",1,211,"https://allnovel.net/the-great-hunt-the-wheel-of-time-2/page-")#50
            print(z[0]+" "+(str)(l)+" #")
         #   h2.execute("UPDATE b01  SET [02]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()
        
kk=1000
q=0
if q==0:
    print("第三部:")
    for z in h3: #爬所有角色第三部之資料   z[11]
        
        if kk==z[8]:     
            inquire(z[9],1770629,55,"https://www.daocaorenshuwu.com/book/zhuanshengzhenlong/")
            
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [03]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()

q=0
if q==0:
    print("第四部:")
    for z in h3: #爬所有角色第四部之資料   z[12]
        
        if  kk==z[8]:
            inquire(z[9],1770688,58,"https://www.daocaorenshuwu.com/book/anyingjianqi/")
            
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [04]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()    

q=0
if q==0:
    print("第五部:")
    for z in h3: #爬所有角色第五部之資料   z[13]
     
       
        if kk==z[8]:      
            inquire(z[9],1770749,57,"https://www.daocaorenshuwu.com/book/tiankongzhihuo/")
            
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [05]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()   

q=0
if q==0:
    print("第六部:")
    for z in h3: #爬所有角色第6部之資料   z[14]
       
        
        if  kk==z[8]:      
            inquire(z[9],1770809,58,"https://www.daocaorenshuwu.com/book/hunchunzhiwang/")
            
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [06]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if q==0:
    print("第七部:")
    for z in h3: #爬所有角色第7部之資料   z[15]
        
        
        if  kk==z[8]:     
            inquire(z[9],1770871,42,"https://www.daocaorenshuwu.com/book/jianzhiwangguan/")
         
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [07]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if q==0:
    print("第八部:")
    for z in h3: #爬所有角色第8部之資料   z[16]
    
        
        if  kk==z[8]:     
            inquire(z[9],1770917,32,"https://www.daocaorenshuwu.com/book/bishouzhilu/")
            
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [08]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if q==0:
    print("第九部:")
    for z in h3: #爬所有角色第8部之資料   z[17]
    
       
        if  kk==z[8]:      
            inquire(z[9],1770951,37,"https://www.daocaorenshuwu.com/book/handongzhixin/")
           
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [09]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit() 

q=0
if q==0:
    print("第十部:")
    for z in h3: #爬所有角色第8部之資料   z[18]
      
        
        if  kk==z[8]:      
            inquire(z[9],1770992,32,"https://www.daocaorenshuwu.com/book/guangyingqilu/")
          
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [10]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()          
            
q=0
if q==0:
    print("第十一部:")
    for z in h3: #爬所有角色第8部之資料   z[19]   
     
        
        if  kk==z[8]:      
            inquire(z[9],1771028,39,"https://www.daocaorenshuwu.com/book/mimengzhiren/")
           
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [11]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()          
                     

q=0
if q==0:
    print("第十二部:")
    for z in h3: #爬所有角色第8部之資料   z[20]   
       
        if  kk==z[8]:     
            inquire(z[9],1771070,52,"https://www.daocaorenshuwu.com/book/morifengbao/")
            
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [12]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()          
                            
q=0
if q==0:
    print("第十三部:")
    for z in h3: #爬所有角色第13部之資料   z[21]   
        
        if  kk==z[8]:      
            inquire(z[9],1771128,60,"https://www.daocaorenshuwu.com/book/wuyegaota/")
           
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [13]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()   
q=0
if q==0:
    print("第十四部:")
    for z in h3: #爬所有角色第14部之資料   z[22]   
        
        if  kk==z[8]:     
            inquire(z[9],1771191,53,"https://www.daocaorenshuwu.com/book/guangminghuiyi/")
         
           
            print(z[0]+" "+(str)(l))
            h2.execute("UPDATE b01  SET [14]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()   

q=0
if q==0:
    print("第一部:")
    for z in h3: #爬所有角色第1部之資料   z[5]   
       
        if  kk==z[8]:     
            inquire(z[9],1770521,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_shang/")
            print(z[0]+" "+(str)(l))
            gg=l
            inquire(z[9],1770548,27,"https://www.daocaorenshuwu.com/book/shijiezhiyan_xia/")
            gg+=l
            print(z[0]+" "+(str)(l)+" "+(str)(gg))
            h2.execute("UPDATE b01  SET [01]="+(str)(gg)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()  

q=0
if q==0:
    print("前傳:")
    for z in h3: #爬所有角色第1部之資料   z[23]   
        
        if kk==z[8]:      
            inquire(z[9],1770492,27,"https://www.daocaorenshuwu.com/book/shiguangzhilun/")
            print(z[0]+" "+(str)(l))
           
            h2.execute("UPDATE b01  SET [00]="+(str)(l)+" WHERE 編號="+(str)(z[8]) )            
            h.commit()  


            
h2.close()
h.close()
print("q5")

		


print("end*******************" , l)