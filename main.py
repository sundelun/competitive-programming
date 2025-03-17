from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
from collections import deque
"""
MX = 32000
is_prime = [True] * (MX + 1)
for i in range(2, MX):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False
 
class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.fw = [0] * (n+1)
    
    def update(self, i: int, delta: int):
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i
    
    def query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
"""
 
def solve():
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    arr.sort()
    # [2, 4]
    # left = 1, right = 4
    # cntleft = 2, cntright = 1
    ans = 0
    for left in range(1, n):
        right = n - left
        cntleft = bisect.bisect_left(arr, left)
        cntright = bisect.bisect_left(arr, right)
        cntleft = m - cntleft
        cntright = m - cntright
        if cntleft == 0 or cntright == 0: continue
        mx = min(cntleft, cntright)
        ans += (cntleft * cntright) - mx
    print(ans)
for _ in range(int(input())):
    solve()