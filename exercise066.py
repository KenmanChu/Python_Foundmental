# -*- encoding:UTF-8 -*-

'''


'''

if __name__ == '__main__':
    n1 = int(input("input a number:\n"))
    n2 = int(input("input a number:\n"))
    n3 = int(input("input a number:\n"))
    
    def swap(p1, p2):
        return p2, p1
    
    if n1 > n2 : n1, n2 = swap(n1, n2)
    if n1 > n3 : n1, n3 = swap(n1, n3)
    if n2 > n3 : n2, n3 = swap(n2, n3)
    
    print (n1, n2, n3)
    
    