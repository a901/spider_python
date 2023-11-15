
import re

import keras

p = re . compile ('(([a-z])*([1-9])*)*' ) #用於匹配至少一個數字
m = p . match ( 'one12twothree34four' ) #查找頭部，沒有匹配

print('0: ',m.group())
print('1: ',m)
print('2: ',m.span())

m.span()
m = p . match ( 'one12twothree34four ' , 2 , 10 ) #從'e'的位置開始匹配，沒有匹配
print('3: ',m)  