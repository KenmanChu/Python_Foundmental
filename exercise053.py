# -*- encoding: UTF-8 -*-
'''
题目：学习使用按位异或 ^ 。

程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
'''

if __name__ == "__main__":
    a = 0x77
    b = a ^ 3
    print ("a ^ 3 is %d" % b)
    b ^= 7
    print ("a ^ b is %d" % b)