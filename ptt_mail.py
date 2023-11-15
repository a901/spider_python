import smtplib
import sys
from email.mime.text import MIMEText
from PTTLibrary  import PTT

PTTBot = PTT.Library(  )
print('login0')
try:
    PTTBot.login('a46911a149', 'A46911a46')
except PTT.Exceptions.LoginError:
    PTTBot.log('登入失敗')
    sys.exit()
except PTT.Exceptions.WrongIDorPassword:
    PTTBot.log('帳號密碼錯誤')
    sys.exit()
except PTT.Exceptions.LoginTooOften:
    PTTBot.log('請稍等一下再登入')
    sys.exit()

print('login')



    
def sendmail(id,k):
    
    k=(str)(k)
    Content1 = '\r\n\n\r\n\n'.join(
        [
            '路過建議',
            '您的文章 '+k,
            '標題可以善用[]格式的標籤哦'
        ]
    )
    Content = '\r\n\n\r\n\n'.join(
        [
            '妳好!',
            '我是男生 ',
            '有興趣聊聊嗎'
        ]
    )

    try:
        PTTBot.mail(
                # 寄信對象
            id,
            # 標題
            '標籤',
            # 內文
            Content,
            # 簽名檔
            0
        )
    
    except PTT.Exceptions.NoSuchUser:
        print('No Such User')
    
def sch(b):
    k=0
    index = PTTBot.getNewestIndex(
        PTT.IndexType.BBS,
        Board=b
    )
    print('最新文章編號:'+str(index))
    for i in range(index-120,index):
        
        Post = PTTBot.getPost(
                b,
                PostIndex=i
        )
        if Post is None:
       #     print('Post is None')
            continue
        if Post.getDeleteStatus() != PTT.PostDeleteStatus.NotDeleted:  
       #     print(f'[不明刪除]')
            continue
        if not Post.isFormatCheck():
      #      print('[不合格式]')
            continue
      
        t=Post.getAuthor().split(' ');
        print(t[0])# 作者id
        
        if 'WomenTalk' not in Post.getContent():
            print('目標文章!!!')
        else:
            #print('無誤!!!')
            continue
        print('Board: ' + Post.getBoard())
        print('Author: ' + Post.getAuthor())
        print('Date: ' + Post.getDate())
        print('Title: ' + Post.getTitle())
        print('文章代碼: ' +  Post.getAID())
        
        print()
        
    
    
def sendmore(b):
    k=0
    index = PTTBot.getNewestIndex(
        PTT.IndexType.BBS,
        Board=b
    )
    print('最新文章編號:'+str(index))
    for i in range(index-20,index):
        
        Post = PTTBot.getPost(
                b,
                PostIndex=i
        )
        if Post is None:
            print('Post is None')
            continue
        if Post.getDeleteStatus() != PTT.PostDeleteStatus.NotDeleted:  
            print(f'[不明刪除]')
            continue
        if not Post.isFormatCheck():
            print('[不合格式]')
            continue
      
        t=Post.getAuthor().split(' ');
        print(t[0])
        
        if '[' not in Post.getTitle():
            print('文章標題標籤有誤!!!')
        else:
            print('無誤!!!')
            #continue
        print('Board: ' + Post.getBoard())
        print('Author: ' + Post.getAuthor())
        print('Date: ' + Post.getDate())
        print('Title: ' + Post.getTitle())
        print('文章推文數: ' + str(Post.getPushNumber()))
        
        
        k=0
        if  k==1:
            sendmail(t[0], Post.getTitle())
            
        if Post.getPushNumber()==None:
            continue
        g= int(Post.getPushNumber())
        
        if g==1010 and k==2:
            sendmail(t[0], Post.getTitle())
           # PTTBot.push(b, PTT.PushType.Push, 'ok', PostIndex=i)
            print('已寄')
        print()
        
    
#sendmore('TaichungBun') 
#sendmore('Wanted')
sch('ID_Multi')
   
#sendmail('a46911a149',1)
#sendmail('a46911a149',2)
PTTBot.logout()











