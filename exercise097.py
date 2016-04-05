#!/usr/bin/python
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    from sys import stdout
    filename = input("input a file name:\n")
    fp = open(filename, 'w')
    ch = input("input a string:\n")
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        cj = input('')
        
    fp.close()