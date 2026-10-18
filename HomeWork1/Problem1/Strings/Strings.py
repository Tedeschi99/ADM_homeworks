#
#
#What's your Name
def print_full_name(first, last):
    print("Hello"+' '+first+' '+last+"!"+' '+"You just delved into python.")
    

if __name__ == '__main__':
#Mutations
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return(string)
if __name__ == '__main__':

#Find a string
def count_substring(string, sub_string):
    result = 0 
    for i in range (len(string) - len(sub_string) + 1):
        if len(string) - i < len(sub_string):
            break
        if string[i:i+len(sub_string)] == sub_string:
            result +=1
    return(result)

if __name__ == '__main__':
#String Validatiors
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

#Text Alignement
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
import textwrap

def wrap(string, max_width):
    result = textwrap.fill(string, max_width)
    return(result)

if __name__ == '__main__':

#Door Mat
if __name__ == '__main__':
    N, M = map(int, input().split())

    # Parte superiore
    for i in range(N // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

    # Parte centrale
    print("WELCOME".center(M, "-"))

    # Parte inferiore
    for i in range(N // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

#
#
#
#Capitalize
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words_list = s.split(" ")
    cap_words = []

    for word in words_list:
        word = word.capitalize()
        cap_words.append(word)

    return " ".join(cap_words)
 
if __name__ == '__main__':

#sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join
def split_and_join(line):
    # write your code here
    words = line.split(" ")
    result = "-".join(words)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#String Formatting
def print_formatted(number):
    width = len(format(number, "b"))

    for i in range(1, number + 1):
        decimal = format(i, "d")
        octal = format(i, "o")
        hexadecimal = format(i, "X")
        binary = format(i, "b")

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexadecimal.rjust(width),
            binary.rjust(width)
        )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)