from typing import List
import math
# https://leetcode.cn/problems/increasing-triplet-subsequence/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        # first represent first num(i)
        # second represent second num(j)
        # always maintain first < second
        first = nums[0]
        second = math.inf
        # iterate over k
        for i in range(1, n):
            # if nums[i] > second: we have answer
            if nums[i] > second: return True
            # otherwise nums[i] <= second
            # if we find that nums[i] > first
            # we will replace first with nums[i]
            # because we need to make second as small as possible while satify second > first
            if nums[i] > first:
                second = nums[i]
            # otherwise nums[i] <= first
            # we make first as small as possible
            else:
                first = nums[i]
        return False