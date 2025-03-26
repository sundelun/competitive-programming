# https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal
class Solution:
    # if s[i] != s[i + 1] then we must need a operation
    # either reversing s[0..i] or s[i + 1...n - 1], we take the minimum
    # the reversing for each operation is independent
    # it will not effect other pairwise's original
    def minimumCost(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n - 1):
            if s[i + 1] != s[i]:
                ans += min(i + 1, n - i - 1)
        return ans