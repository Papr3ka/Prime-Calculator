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
    if waitsetc == 2:
        wait = str(input("Press enter to continue..."))
        clear()
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
    clear()
    global primes;
    print("Calculating...")
    primes = [2]
    pcrh = 1
    for prch in range(1,maxprch,2):
        if checkprime(prch):
            trueprime = prch
            primes.append(trueprime)
    for x in primes:
        print(x)
    clear()
    print("Done")
    print("\nLength", len(primes))
    print("Largest Prime", primes[len(primes) - 1])
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
waitsetc = 2
wait()
print("Select View options")
print("1:Range\n2:Approximate\n3:All")
option2 = int(input("Option:"))
clear()
if option2 == 1:
    print("Largest Prime",primes[len(primes)-1],"\n")
    min_r_viewpr = int(input("Minimum:"))
    max_r_viewpr = int(input("Maximum:"))
    clear()
    for cnpr in range(1,len(primes)-1,1):
        if primes[cnpr] >= min_r_viewpr:
            print(primes[cnpr])
        if primes[cnpr + 1] >= max_r_viewpr:
            break
if option2 == 2:
    low_v = 48
    high_v = 48
    ar_viewpr = int(input("Primes near:"))
    if ar_viewpr - low_v <= 1:
        for x in range(1,low_v,1):
            low_v -= 1
            if ar_viewpr - low_v <= 1:
                break
    if ar_viewpr + high_v >= len(primes):
        for x in range(1,high_v,1):
            high_v -= 1
            if ar_viewpr + high_v >= len(primes):
                break
    for cnpr in range(1,len(primes) - 1,1):
        if primes[cnpr] >= ar_viewpr -low_v:
            print(primes[cnpr])
        if primes[cnpr + 1] >= ar_viewpr + high_v:
            break
if option2 == 3:
    for x in primes:
        print(x)
waitsetc = 0
wait()
