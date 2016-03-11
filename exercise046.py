# -*- encoding: UTF-8 -*-
 
'''
题目： 求输入数字的平方，如果平方运算后小于50则退出
分析： 无
'''

TRUE = 1
FALSE = 0
def SQ(x):
    return x * x

print("If the number input less than 50, program will exit")
again = 1
while again:
    num = int(input("please input number:\n"))
    print ("Result is %d" % (SQ(num)))
    if num >= 50:
        again = TRUE
    else:
        again = FALSE