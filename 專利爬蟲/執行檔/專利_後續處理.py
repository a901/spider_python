# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:51:33 2023

@author: a4691
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print ('start\n\n')

total=0


x='x'
table= [[x for i in range(40)] for j in range(170)]
tn=0



for x in range(257):
    
    print('\nx='+str(x+1)+'\n\n')
    name='ff'+str(x+1)+'.txt'
    f = open(name,'r',encoding="utf-8")

    ff=f.readlines()
    f.close()
    
    
    h=ff[2]
    
    line=h
    print(h)
    g=h.split('(',1)
    if len(g)>1:
        check=0
        g=g[1].split(')',1)  ## 讀取第三行括號中的內容
    
        h=g[0]
        print(h)
    else:
        h=''
    
    
    check=0
    for i in h:
        if i=='B':
            check=1
        
    if check==1:
        print('Yes this one')
        total+=1
    else:
        print('not this')
        continue
    
    
    table[tn][0]=line
    for i in range(21,58,1):
        print(ff[i]+' l='+str(len(ff[i])))
        if len(ff[i])<7:
            k=1
        else:
            k=0
        table[tn][i-21+1]=ff[i]
        
    tn+=1
    
    
df = pd.DataFrame(table, columns = ['Name',
                                    'AT','BE','BG','CH','','','','','',
                                    '','','','','','','','','','',
                                    '','','','','','','','','','',
                                    '','','','','','','','','',''])

file_name = '專利.xlsx'
  
# saving the excelsheet
df.to_excel(file_name)


print('\n\n-----------------------\n\n')

print('total= '+str(total))

print('\n\n--------table---------------\n\n')

print(df)


print('\n\n--------ok---------------\n\n')




print('\n\n--------next---------------\n\n')



ar=''

for x in table:
    ar+=str(x)+'\n\n'

ar+='\n\n\n\n'+'total= '+str(total)

f = open('table.txt','w')

f.write(ar)
f.close()

print('\n\n--------end---------------\n\n')



