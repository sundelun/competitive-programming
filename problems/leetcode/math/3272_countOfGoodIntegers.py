import math
from collections import Counter
# https://leetcode.cn/problems/find-the-count-of-good-integers/
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fac = [math.factorial(i) for i in range(n + 1)]
        # fac[i] is equal to i!
        ans = 0
        vis = set()
        base = 10 ** ((n - 1) // 2)
        # we are iterating over all integers with length n
        for i in range(base, base * 10):
            s = str(i)
            # s is palindrome
            s += s[::-1][n % 2 :]
            # s must be divisible by k
            if int(s) % k: continue
            # sort the integer s then see if we used this permutation before
            record = ''.join(sorted(s))
            if record in vis: continue
            vis.add(record)
            # now we need to count how many arragements is possible for integer s
            cnt = Counter(record)
            # because we cannot have leading zero
            res = (n - cnt['0']) * fac[n - 1]
            # same as combination math
            # we divid by (num_of_duplicate)!
            for c in cnt.values():
                res //= fac[c]
            ans += res
        return ans