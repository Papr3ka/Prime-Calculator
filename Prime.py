# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import os
import platform
import math
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def checkprime(x):
    if x >= 2:
        for y in range(2,x):
            if not( x % y ):
                return False
    else:
        return False
    return True
clear()
minprch = int(input("Minimum Prime"))
maxprch = int(input("Maximum Prime"))
clear()
prch = minprch
for prch in range(minprch,maxprch,1):
    if checkprime(prch) == True:
        print(prch)
