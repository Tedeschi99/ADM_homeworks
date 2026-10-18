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