#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
列表使用实例。

'''

#list
#create List
testList = [10086, 'China Mobile', [1,2,4,5]]

#list length
print (len(testList))
# to end of the List
print (testList[1:])
#add element to List
testList.append('i\'m new here!')

print (len(testList))
print (testList[-1])

print (testList.pop(1))
print (len(testList))

print (testList)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print (matrix)
print (matrix[1])
co12 = [row[1] for row in matrix]
print (co12)
co12even = [row[1] for row in matrix if row[1] % 2 == 0 ]
print (co12even)