# https://leetcode.cn/problems/count-partitions-with-max-min-difference-at-most-k/description/
from typing import List
from collections import deque
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        O(N^2) solution:
        f[i + 1] represent number of partitions end with nums[i]
        f[i + 1] = sumof(f[j]) j range from L to i, where L is the first index such that nums[L:i] satisfy the condition

        Optimize time complexity with monotonic queue
        we will only record the maximum and minimum along a subarray
        the shorter the subarray it will satisfy max - min <= k
        so we can use a two-pointer to record all valid partitions in this window
        """
        mod = 10 ** 9 + 7
        mn_st = deque()
        mx_st = deque()
        # sum_f is the number of partitions of f[i + 1]
        # left-pointer to record all invalid partitions
        sum_f = left = 0
        n = len(nums)
        f = [0] * (n + 1)
        f[0] = 1
        for i, num in enumerate(nums):
            sum_f += f[i]
            # pop the useless element that used in min_queue
            while mn_st and num <= nums[mn_st[-1]]:
                mn_st.pop()
            mn_st.append(i)
            # pop the useless element that used in max_queue
            while mx_st and num >= nums[mx_st[-1]]:
                mx_st.pop()
            mx_st.append(i)
            # pop the partitions not satisfy the valid partitions
            while nums[mx_st[0]] - nums[mn_st[0]] > k:
                # remove f[left] numbr of partitions
                sum_f -= f[left]
                left += 1
                # if our left-most index from min_queue/max_queue is outside of left pointer
                # we will pop it
                if left > mn_st[0]:
                    mn_st.popleft()
                if left > mx_st[0]:
                    mx_st.popleft()
            # record answer
            f[i + 1] = sum_f % mod
        return f[n]