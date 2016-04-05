#!/usr/bin/python
#-*-coding:utf=8 -*-

if __name__ == '__main__':
    import time
    import random
    
    play_it = input("do you wnat to paly it:(\'y\' or \'n\')")
    while play_it == 'y':
        c = input ("input a character:\n")
        i = random.randint(0, 2**32) % 100
        start = time.clock()
        a = time.time()
        guess = int(input("input your guess:\n"))
        while guess != i:
            if guess > i :
                print ("please input a little smaller\n")
                guess = int(input("input your guess:\n"))
            else:
                print ("please input a litter bigger:\n")
                guess = int(input("input your guess:\n"))
                
    end = time.clock()
    b = time.time()
    var = (end - start) / 18.2
    print (var)
    
    if var < 15:
        print ("you are very clever\n")
    elif var < 25:
        print ("you are normal\n")
    else:
        print ("you are stupid\n")
        
    print ("Congratulatins")
    print ("The number you guess is %d" %i )
    play_it = input("do you want play it\n")
                           
    