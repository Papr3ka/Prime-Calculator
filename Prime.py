# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import os
import system
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def checkprime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True
