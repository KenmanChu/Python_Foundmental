# -*- coding: UTF-8 -*-

'''
题目：按相反的顺序输出列表的值
'''

a = ['one','two','three']
for i in a[::-1]:
    print (i)
    
    
for i in a[::1]:
    print (i)
    
for i in a[::]:
    print (i)