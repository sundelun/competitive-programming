from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        if (a + b) mod k = (b + c) mod k
        then (a + b - (b + c)) mod k = 0
        then (a - c) mod k = 0
        it means a and c modulo k is same
        which means sub[i] and sub[i + 2] modulo k is same
        for a valid subsequance sub[0], sub[2], sub[4],... modulo k are same
        and sub[1], sub[3], sub[5],... modulo k are same
        this question translates to longest subsequence such that odd-index have same remainder modulo k
        and even-index have same remainder modulo k

        define f[x][y] as the last two elements who modulo are y and x respectively
        if x = nums[i] % k, then f[x][y] = f[y][x] + 1
        """
        f = [[0] * k for _ in range(k)]
        for num in nums:
            x = num % k
            for y in range(k):
                f[x][y] = f[y][x] + 1
        return max(map(max, f))