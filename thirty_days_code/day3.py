#!/bin/python
"""Intro to Conditionals"""

import sys


N = int(raw_input().strip())

if N % 2 == 1:  # N is odd
    print "Weird"

elif N % 2 == 0:  # N is even and:
    if N in range(6, 21):  # 6 <= N <= 20: Weird
        print "Weird"
    else:  # N < 6 or N > 20: Not Weird
        print "Not Weird"
