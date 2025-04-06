# https://leetcode.cn/problems/valid-triangle-number/description/
from typing import List
class Solution:
    # first method, iterate the longest side with opposite direction two-pointers
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        # iterate over the longest side of 3
        for i in range(n - 1, 1, -1):
            # optimization at first
            # all nums[i] as longest side will make 0 triangles
            if nums[i] >= nums[i - 1] + nums[i - 2]:
                continue
            # all nums[i] as longest side will make triangles
            # because we are iterating in reverse order
            # we can just calculate all number of pairs here
            if nums[i] < nums[0] + nums[1]:
                # same as comb(i + 1, 3)
                ans += (i + 1) * i * (i - 1) // 6
                break
            # two-pointer technique
            left = 0
            right = i - 1
            while left < right:
                # if nums[left] + nums[right] <= nums[i]
                # then nums[left] + nums[right - 1]
                # .... nums[left] + nums[left] + 1 also <= nums[i]
                # so we need to make left += 1
                if nums[i] >= nums[left] + nums[right]:
                    left += 1
                # if nums[left] + nums[right] > nums[i]
                # then nums[left + 1] + nums[right] > nums[i]
                # ....nums[right - 1] + nums[right] > nums[i]
                # there a are a total of right - left valid answer
                # and eventually we make right -= 1
                else:
                    ans += right - left
                    right -= 1
        return ans
    
class Solution:
    # second method, iterate over shortest side with same direction two-pointer
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        # iterate over the shortest side
        for i in range(n - 2):
            if nums[i] == 0: continue
            k = i + 2
            # j is second-longest side
            for j in range(i + 1, n - 1):
                # while there can be a triangle
                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1
                # if nums[k - 1] < nums[i] + nums[j]
                # then nums[k - 2], nums[k - 3] ... nums[j + 1] all < nums[i] + nums[j]
                # so we have total of k - 1 - j valid triangles
                ans += k - j - 1
        return ans