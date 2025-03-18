# https://codeforces.com/contest/2053/problem/C
"""
if we call the process of splitting a large segment into two smaller segments a round, then all segments are of the same length when the i
-th round of the observation is conducted, and the number of rounds does not exceed O(logN)
"""
from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
def solve():
    """
    Note that the distribution of segments after round 1 is centrally symmetric; Also, x and y
    being centrally symmetric implies that x+y=n+1
    , so it is simple to calculate by simulating the number of segments and the length directly.
    time complexity: O(tlogN)
    """
    n, k = map(int, input().split())
    ans = 0
    mul = n + 1
    # ans is number of segments we will be recorded
    # because it is going symetrically, so all things will be parallel, for example if we have [1, 15] next we have[1,7] and [9, 15]
    # [1, 15] will contibute 8 to answer, and [1, 7] will contibute 4, while [9, 17] will contribute 12 (2nd layer total of 16)
    # and 3rd layer will then contribute total of 32...
    # so we notice that each layer is same as  sumof (n + 1) * (# of segments in currentlayer) // 2
    # we can iterate over O(logN) and count total # of segments and divide by 2 at last
    # because it is symmetric, i.e.: always even for all segments or always odd for all segments for each layer of recursion
    cur = 1
    while n >= k:
        # equivalante to n is odd
        if n & 1: ans += cur
        # eqivalance to n //= 2
        n >>= 1
        # equivalance to cur *= 2
        cur <<= 1
    print(mul * ans // 2)
for _ in range(int(input())):
    solve()
