# https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # how many numbers start with prefix p that are less than or equal to n
        # for example if we have call count(1, 13) then it would give me 5 as [1, 10, 11, 12, 13] are included
        def count(p: int, n: int) -> int:
            res = 0
            # nxt does not start with p
            first, nxt = p, p + 1
            while first <= n:
                # each time we exclude those does not start with p
                res += min(n + 1, nxt) - first
                first *= 10
                nxt *= 10
            return res
        curr = 1
        k -= 1
        while k:
            # if k is greater than or equal to number of integer with prefix curr
            # then our answer does not start with prefix curr
            # we add curr by one and k minus count of integer start with prefix curr
            cnt = count(curr, n)
            if cnt <= k:
                curr += 1
                k -= cnt
            # if k is less than number of integer with prefix curr
            # then our answer starts with prefix curr
            # we try to find the smallest one first, which is we minus k by one and multiply curr by 10
            # 
            else:
                curr *= 10
                k -= 1
        return curr