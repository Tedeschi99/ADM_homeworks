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


#runner up
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    top  = arr[0]
    runner = 0
    arr.sort(reverse=True)
    for i in range(0,n):
        if top < arr[i]:
            top = arr[i]
        if arr[i] != top:
            runner = arr[i]
            break      
    print(runner)

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(result)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")

#Lists
if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            arr.insert(int(command[1]), int(command[2]))

        elif operation == "print":
            print(arr)

        elif operation == "remove":
            arr.remove(int(command[1]))

        elif operation == "append":
            arr.append(int(command[1]))

        elif operation == "sort":
            arr.sort()

        elif operation == "pop":
            arr.pop()

        elif operation == "reverse":
            arr.reverse()

#Nested Lists
if __name__ == '__main__':
    Students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        Students.append([name, score])

    scores = [student[1] for student in Students]
    scores = sorted(set(scores))

    names = []

    for x in Students:
        if x[1] == scores[1]:
            names.append(x[0])

    names.sort()

    for i in names:
        print(i)

 #Tuples
 if __name__ == '__main__':
    n = int(raw_input())
    t = tuple(map(int, raw_input().split()))
    print hash(t)

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

#Introduction to Sets

def average(array):
    unique = set(array)
    return round(sum(unique) / len(unique), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#Symmetric Difference

if __name__ == '__main__':
    m = int(input())
    M = set(map(int, input().split()))

    n = int(input())
    N = set(map(int, input().split()))

    result = sorted(M.symmetric_difference(N))

    for x in result:
        print(x)

#Set .add()
if __name__ == '__main__':
    N = int(input())
    countries = set()

    for _ in range(N):
        country = input()
        countries.add(country)

    print(len(countries))

#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    command = input().split()

    if command[0] == "pop":
        s.pop()

    elif command[0] == "remove":
        s.remove(int(command[1]))

    elif command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))

#collections.Counter()
from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        earnings += price
        shoes[size] -= 1

print(earnings)

#DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())

positions = defaultdict(list)

# Lettura del gruppo A
for i in range(1, n + 1):
    word = input()
    positions[word].append(i)

# Lettura del gruppo B
for _ in range(m):
    word = input()

    if word in positions:
        print(*positions[word])
    else:
        print(-1)

#

#Calendar Day

import calendar

month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)

print(calendar.day_name[weekday].upper())

#TimeDelta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"

    date1 = datetime.strptime(t1, format)
    date2 = datetime.strptime(t2, format)

    delta = abs((date1 - date2).total_seconds())

    return str(int(delta))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)

#Detect Floating Point Number
import re

x = int(input())

for i in range(x):
    y = input()
    print(bool(re.fullmatch(r"[+-]?\d*\.\d+", y)))

#Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(), Groups() & Groupdict()
import re

x = (input())

duplicate  = re.search(r"([a-zA-Z0-9])\1",x)

if duplicate:
        print(duplicate.group(1))
else:
    print(-1)

#Re.findall() & Re.finditer()

import re

s = input()

matches = re.findall(
    r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',
    s
)

if matches:
    print("\n".join(matches))
else:
    print(-1)

#Re.start() & Re.end()

import re

x = input()
k = input()

matches = list(re.finditer(rf"(?=({re.escape(k)}))", x))

if matches:
    for i in matches:
        print((i.start(1), i.end(1) - 1))
else:
    print((-1, -1))



#Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating Phone Numbers
regex_pattern = r"^([7,8,9])([0-9]{9}$)"    

import re
n = int(input())

for i in range(n):
    x = (bool(re.match(regex_pattern, input())))
    
    if x:
        print("YES")
    else:
        print("NO")


#Validating and Parsing Email Addresses
regex_pattern = r"[a-zA-Z]+[a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"  

import re
import email.utils
n = int(input())

for _ in range(n):
    line = input()

    name, address = email.utils.parseaddr(line)

    if re.fullmatch(regex_pattern, address):
        print(email.utils.formataddr((name, address)))

#Hex Color Code
regex_pattern = r"[#]{1}([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$"  

import re
import cssutils
n = int(input())

for _ in range(n):
    line = input()


#Validating UID

import re

regex_pattern = r"^(?=(?:.*[A-Z]){2})(?=(?:.*[0-9]){3})(?!.*(.).*\1)[a-zA-Z0-9]{10}$"

T = int(input())

for _ in range(T):
    uid = input()

    if re.fullmatch(regex_pattern, uid):
        print("Valid")
    else:
        print("Invalid")

#Regex Substitution


#Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        ordered = sorted(people, key=lambda person: int(person[2]))
        return [f(person) for person in ordered]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#Arrays
import numpy

def arrays(arr):
    res = numpy.array(arr,float)
    result = numpy.flip((res))
    return result


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape

import numpy

arr = input().strip().split(' ')

result  =  numpy.array(arr, dtype = int)

print (numpy.reshape(result,(3,3)))

#Transpose and Flatten
import numpy as np

N, M = map(int, input().split())

matrix = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

print(np.transpose(matrix))
print(matrix.flatten())


#Eye and Identity
import numpy

numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(numpy.eye(N, M))

#Array Mathematics
import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

B = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

#Sum and Prod
import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

sums = np.sum(A, axis=0)

result = np.prod(sums)

print(result)

#Min and Max

import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

minimums = np.min(A, axis=1)

result = np.max(minimums)

print(result)

#Mean, Var, and Std
import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(round(np.std(A), 11))


import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    x = max(candles)
    result = candles.count(x)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):

    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    base = 5
    like = 0
    result = 0

    for i in range(n):
        
        dailylike  = base // 2 
        like = dailylike
        base = like * 3
        
        result += like
    
    return(result)
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    result = 0

    for i in str(n):
        result += int(i)

    result = result * k

    if len(str(result)) > 1:
        return superDigit(result, 1)

    return result
        



    


    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    key = arr[n-1]
    
    j = n-2
    
    while j >= 0 and arr[j] > key:
        arr[n-1] = arr[j]
        
        print(*arr)
        n -= 1
        j -= 1
        
    arr[j+1] = key
    print (*arr)
    return arr
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    k = len(arr)
    for i in range(1,k):
        key = arr[i]
        j = i-1
    
        while j >= 0 and arr[j] > key:
            
            arr[j+1] = arr[j]
            
            j -= 1
            
        arr[j + 1] = key
        print(*arr)
        
        
    
    return arr

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)