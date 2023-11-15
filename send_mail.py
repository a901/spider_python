import smtplib
from email.mime.text import MIMEText
from PTTLibrary  import PTT
import t1




aa()
aa()
PTTBot = PTT.Library()

ErrCode = PTTBot.login('a4691s1a149', 'A46911a46911')
print('login')


sendmail('a46911a149')
sendmail('a46911a149')
    
def sendmail(id):
    
    Content = '\r\n\r\n'.join(
        [
            '這是一封測試信，若誤寄請見諒',
            'PTT Library 程式寄信測試內容',
            ''
        ]
    )

    try:
        PTTBot.mail(
                # 寄信對象
            id,
            # 標題
            '標題',
            # 內文
            Content,
            # 簽名檔
            0
        )
        except PTT.Exceptions.NoSuchUser:
            print('No Such User')
    
    
gmail_user = 'a46911a149@gmail.com'
gmail_password = 'A46911a46911' # your gmail password
print('Email 1')


m='content文字'
m = m.encode('big5')
print(m)
m='文字'


msg = MIMEText('A94DA5AD')
msg['Subject'] = 'Test'
msg['From'] = gmail_user
msg['To'] = 'a46911a149.bbs@ptt.cc' #a46911a149.bbs@ptt.cc

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

print('Email 2')
server.ehlo()
server.login(gmail_user, gmail_password)

print('Email 3')
#server.send_message(msg)
server.quit()

print('Email sent!')




