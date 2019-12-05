# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import os
import platform
import math
waitsetc = 0
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def wait():
    if waitsetc == 1:
        clear()
        wait = str(input("Press enter to continue..."))
    if waitsetc == 0:
        wait = str(input("Press enter to exit..."))
    clear()
def checkprime(x):
    if x >= 2:
        for y in range(2,x):
            if not( x % y ):
                return False
    else:
        return False
    return True
def normprcalc():
    prch = minprch
    for prch in range(minprch,maxprch,1):
        if checkprime(prch) == True:
            print(prch)
def lucaslehmer():
    prch
clear()
print("Select Primality Algorithm")
print("1:Normal Prime\n2:lucas Lehmer")
option = int(input("Option:"))
clear()
minprch = int(input("Minimum Prime:"))
maxprch = int(input("Maximum Prime:"))
clear()
if option == 1:
    normprcalc()
if option == 2:
    
