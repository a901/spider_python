
from urllib.request import urlopen
from bs4 import BeautifulSoup

import opencc

import torch

g=[]
k="asdfag"
for z in range(100):
    g.append(0)
    
h='a'
for z in range(5):
    if h==k[z]:
        g[z]=1
        print(z)
    
g="村子里没有人会怀疑住在这间暖洋洋的房子里的两位老姐妹会是两仪师。谁也不会想到在提凡井这样的小地方会有两仪师出现，这里不过是艾拉非草原深处的一个小农庄而已。村民们经常会找两姐妹咨询问题，求治病症，她们在村民眼中只是两位受到光明祝福的女子而已。艾迪莉丝和凡迪恩隐退已久，就算在白塔里，也没有几个人记得她们还活着。 "

cc = opencc.OpenCC('s2t')
g=cc.convert(g)

print(g)



# t2s -繁體轉簡體（Traditional Chinese to Simplified Chinese）
# s2t -簡體轉繁體（Simplified Chinese to Traditional Chinese）


#from BeautifulSoup import BeautifulSoup

#html = urlopen ("file:///C:/Users/Chi%20Yun%20Lee/Desktop/aaaa.html")

#print(html.read())

#a = BeautifulSoup(html.read())
#print(a.h1)
for z in range(10,20):
    print(z)