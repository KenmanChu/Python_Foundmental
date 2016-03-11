# -*- coding: UTF-8 -*-

'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。

'''

x = int(input('input a number:\n'))

a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10

if a != 0:
    print('it is a 5 digit number: %d%d%d%d%d' % (e, d, c, b, a))
elif b != 0:
    print('it is a 4 digit number %d%d%d%d' % (e, d, c, b))
elif c != 0:
    print('it is a 3 digit number %d%d%d' % (e, d, c))
elif d != 0:
    print('it is a 2 digit number %d%d' % (e, d))
else:
    print('it is a 1 digit number %d' % e)