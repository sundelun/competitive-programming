from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # the challenge here is we need to exclude the duplicate answer
        # for example we have [1, 1, 1, 2]
        # then if we fill ans[0] with nums[0]
        # then we cannot fill ans[0] with either nums[1] and nums[2]
        # because otherwise we would be guaranteed to have duplicate permutations
        # therefore, we only need to fill the first blank with choice of just one of 
        # all same number 
        # first sort the nums
        nums.sort()
        ans = []
        n = len(nums)
        res = []
        # whether nums[i] have been used
        path = [False] * n
        def dfs(i: int) -> None:
            if i == n:
                ans.append(res.copy())
                return
            for j, on in enumerate(path):
                if on: continue
                # if the nums[j] is same as previous one and previous one have not been filled
                # we cannot fill with nums[j], otherwise duplicate will occur
                # for example if we have nums = [1,1,2] and now we are at j = 1
                # and path[0] = False, if we fill ans[0] = nums[1]
                # then there is a possibility that ans[1] = nums[0]
                # which is same as ans[0] = nums[0] and ans[1] = nums[1]
                if j > 0 and nums[j] == nums[j - 1] and not path[j - 1]: continue
                res.append(nums[j])
                path[j] = True
                dfs(i + 1)
                path[j] = False
                res.pop()
        dfs(0)
        return ans