# https://leetcode.cn/problems/3sum/description/
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for a, num in enumerate(nums[:n - 2]):
            # we will only continue if they are not same from pevious, otherwise it would contain dupliecate
            # for example [-2, -2, -2, 1, 1] will have duplicate
            if a and num == nums[a - 1]: continue
            # optimize, if a + max(b + c) < 0 then all of the choose of a will be impossible, so continue
            if num + nums[-2] + nums[-1] < 0: continue
            # optimize, if this is the smallest 3 sum we can get, then just return answer because not possible to find any smaller
            if num + nums[a + 1] + nums[a + 2] > 0: break
            b = a + 1
            c = n - 1
            while b < c:
                if num + nums[b] + nums[c] > 0:
                    c -= 1
                elif num + nums[b] + nums[c] < 0:
                    b += 1
                else:
                    ans.append([num, nums[b], nums[c]])
                    # we must get rid of duplicates in the inner two-pointer as well
                    # continue until we find a not same as recorded answer for both b and c
                    stb = b
                    while b < c and nums[b] == nums[stb]:
                        b += 1
                    stc = c
                    while b < c and nums[c] == nums[stc]:
                        c -= 1
        return ans