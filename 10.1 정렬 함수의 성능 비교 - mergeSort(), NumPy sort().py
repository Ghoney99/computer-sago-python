# HW 10.1 정렬 함수의 성능 비교 - mergeSort(), NumPy sort()
# Author : 장지헌
# Date : 2023. 5. 10.
# Features :
# - performance comparisons of mergeSort() and Numpy sort()

import os, sys, random, time
import numpy as np
from MyList import *
from MySortings import *
# HW 10.1 Big rand list with mergeSort and np.sort (1)
#------------------------------------------
def main():
    num_sample_Lines = 2
    num_elements_per_Line = 10
    test_sizes = [100000, 1000000, 10000000]
    
    for size_L in test_sizes:
        L = genRandList(size_L)
        print("\nBefore mergeSort of L (size: {}):".format(size_L))
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        t1 = time.time()
        mergeSort(L)
        t2 = time.time()
        print("After mergeSort of L :")
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        time_elapsed = t2 - t1
        print("mergeSort() for list L (size = {}) took {} sec".format(size_L, time_elapsed))
        print("\nBefore np.sort of L (size: {}):".format(size_L))
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        t1 = time.time()
        np.sort(L)
        t2 = time.time()
        print("After np.sort of L :")
        printListSample(L, num_elements_per_Line, num_sample_Lines)
        time_elapsed = t2 - t1
        print("np.sort() for list L (size = {}) took {} sec".format(size_L, time_elapsed))
if __name__ == "__main__":
    main()