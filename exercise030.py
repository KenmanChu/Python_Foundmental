# -*- coding: UTF-8 -*-
'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。

'''

a = int(input('input a number:\n'))
x = str(a)
flag = True

for i in range(len(x)/2):
    if x[i] != x[-i-1]:
        flag = False
        break
    
if flag:
    print ("%d is a palindrome" % i)
    