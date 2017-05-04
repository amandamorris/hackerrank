"""Given an integer from standard in, print the maximum number of contiguous
1s in the binary representation of that integer."""

#!/bin/python

import sys


n = int(raw_input().strip())
binary = "{0:b}".format(n)  # binary representation of n

max1s = 0  # to track the length of the longest string of 1s
count = 0  # to count the current string of 1s

for char in binary:  # iterate through the binary representation
    if char == "1":
        count += 1  # increment count for each 1
        if count > max1s:  # if the count is greater than the current max:
            max1s = count  # set max1s to current count
    else:
        count = 0  # reset count if char == 0
print max1s
