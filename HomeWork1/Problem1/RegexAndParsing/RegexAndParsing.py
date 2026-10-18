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
