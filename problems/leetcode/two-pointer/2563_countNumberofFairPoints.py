# https://leetcode.cn/problems/count-the-number-of-fair-pairs/
# same question as codeforced div3 round 995 D: https://codeforces.com/contest/2051/problem/D
from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        # as nums[j] becomes bigger, lower - nums[j] and upper - nums[j] becomes smaller
        # we can use a 3-pointer technique to solve!
        left = right = len(nums)
        for j, x in enumerate(nums):
            # right is the point that satisfy nums[right - 1] <= upper - x
            while right and nums[right - 1] > upper - x:
                right -= 1
            # left is the point that satisfy nums[left - 1] < lower - x
            while left and nums[left - 1] >= lower - x:
                left -= 1
            # same as binary search method, we need to make sure both right and left <= j
            ans += min(right, j) - min(left, j)
        return ans