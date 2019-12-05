# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import os
import platform
waitsetc = 1
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
        for y in range(2,x,1):
            if not( x % y ):
                return False
    else:
        return False
    return True
def normprcalc():
    primes = [2]
    pcrh = 1
    for prch in range(1,maxprch,2):
        if checkprime(prch):
            trueprime = prch
            primes.append(trueprime)
            print(trueprime)
    for x in primes:
        print(x)
clear()
print("Select Primality Algorithm")
print("1:Normal Prime")
option = int(input("Option:"))
clear()
maxprch = int(input("Maximum Prime:"))
clear()
if option == 1:
    wait()
    normprcalc()
waitsetc = 0
wait()
