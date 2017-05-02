#!/bin/python
"""prints array in reverse order, on a single line"""

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for num in arr[::-1]:
    print num,