from typing import List
import math
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        mx = -math.inf
        mn = math.inf
        ansl = ansr = -1
        n = len(array)
        # if on the left hand side we have element greater than array[i]
        # then a[i] must be included in the answer
        # we need to find the right-most element that have some element greater than a[i]
        # the index that is greater than a[i] is guaranteed to be included in answer in second iteration
        for i in range(n):
            if array[i] < mx: ansr = i
            else: mx = array[i]
        # if on the right hand side we have element smaller than array[i]
        # then a[i] must be included in the answer
        # we need to find the left-most element that have some element smaller than a[i]
        for i in range(n - 1, -1, -1):
            if array[i] > mn: ansl = i
            else: mn = array[i]
        return [ansl, ansr]