# https://github.com/iordakis/
# A simple iterative way of finding any missing integer in a sorted array
import numpy as np

# example array with missing integers (a list can also be used)
array = np.array([1,2,4,5,6,7,8,9,11,12,15,19,33,35])

C = 0
incr = 1

for x in range(len(array)-1):
    if array[C] - array[C+1] <= -1:
        for x in range(array[C+1] - array[C] - 1):
            print(array[C]+incr, 'is missing')
            incr = incr +1
        incr = 1
    C = C+1
