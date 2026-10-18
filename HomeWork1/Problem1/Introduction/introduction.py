#if __name__ == '__main__':
#Say hello world
print("Hello, World!")



# Arithmetic Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)


#Python: Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)

#Loops
n = int(input())
L = []
for i in range(n):
        L.append(i)
for k in range(len(L)):
        print(L[k]*L[k])

#Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    
    
    
    return leap

year = int(input())

#Print Function
n = int(input())
for i in range(1,n+1):
    print(i, sep=' ', end='')

#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())


odd = False
if n % 2 != 0:
    print("Wierd")
    odd = True
if n >= 2 and n <= 5 and not odd:
    print("Not Weird")
elif n >= 6 and n <= 20 and not odd:
    print("Wierd")
elif n > 20 and not odd:
    print("Not Wierd") 
