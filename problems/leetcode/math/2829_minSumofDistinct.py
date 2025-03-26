# https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description/
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        # [1,2,3,4,5] but 1 + 3 equal to 4
        # n = 10, k = 8 [1,2,3,4,5,6,7,8,9,10] -> {(1, 8), (2, 7), (3, 6), (4, 5)} equal to 9
        # -> 5, 6, 7, 8 should not exsist in list change to 11, 12, 13, 14
        # for every pair with sum equal to k, we choose the smaller number
        # so the first part of result array is m * (m + 1) // 2
        # where m = min(k // 2, n), because the dropping element of pair begin with k // 2 + k % 2
        m = min(k // 2, n)
        ans = m * (m + 1) // 2
        # there are n - m number left, and start with k(all number >= k)
        # so the second part of answer is from k to k + n - m - 1
        # by the math formula, the sum within range of [k, k + n - m - 1] is
        # (2k + n - m - 1)(n - m) // 2
        # since the sum from range[x,y] is equal to (x + y) * (y - x + 1) // 2
        return ans + (2 * k + n - m - 1) * (n - m) // 2