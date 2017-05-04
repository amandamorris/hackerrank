"""Given a 6x6 matrix, and an hourglass shape:
X X X
  X
X X X
This file calculates the sum of values for each hourglass in the array, and
prints the maximum sum"""

import sys


arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

def hourglass_sum(array, upperleft):
    """Given an array and the coordinates corresponding to the upper left corner
    of an hourglass, return the sum of values in the hourglass"""

    topsum = array[upperleft[0]][upperleft[1]] + array[upperleft[0]][upperleft[1] + 1] + array[upperleft[0]][upperleft[1] + 2]
    bottomsum = array[upperleft[0] + 2][upperleft[1]] + array[upperleft[0] + 2][upperleft[1] + 1] + array[upperleft[0] + 2][upperleft[1] + 2]
    middle = array[upperleft[0] + 1][upperleft[1] + 1]

    return topsum + bottomsum + middle


max_sum = hourglass_sum(arr, (0,0))  # initialize max_sum to be the sum of the
                                     # upper left hourglass

# iterate through each element in the array (leaving a buffer of right two
# columns and bottom two rows), call hourglass_sum, update the max
for row in range(len(arr) - 2):
    for col in range(len(arr[0]) - 2):
        hg_sum = hourglass_sum(arr, (row, col))
        if hg_sum > max_sum:
            max_sum = hg_sum
print max_sum