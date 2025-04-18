from typing import List
import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # order does not matter because it is just reqreuing two numbers
        # so we can sort the nums
        nums.sort()
        ans = 0
        # lower <= nums[i] + nums[j] <= upper
        # lower - nums[j] <= nums[i] <= upper - nums[j]
        # therefore, we need to count number of nums[i] that is less than or equal to upper - nums[j]
        # minus number of nums[i] that is less than lower - nums[j]
        # we will be iterating over index j
        # and on the range of nums[0, j - 1] we will be doing the binary search
        # because the question ask to make i < j, iterate over every j to find all validate i with respect to this j
        for j, num in enumerate(nums):
            left = bisect.bisect_left(nums, lower - num, 0, j)
            right = bisect.bisect_right(nums, upper - num, 0, j)
            ans += right - left
        return ans