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
    n = int(input())
    record = []
    cnt = [0] * (2 * n + 1)
    cnt2 = [0] * (2 * n + 1)
    for _ in range(n):
        l, r = map(int, input().split())
        record.append([l, r])
        if l == r: 
            cnt[l] = 1
            cnt2[l] += 1
    ans = []
    prefix = list(accumulate(cnt, initial = 0))
    for x, y in record:
        if x == y:
            if cnt2[x] > 1: ans.append('0')
            else: ans.append('1')
        else:
            if prefix[y + 1] - prefix[x] == y - x + 1: ans.append('0')
            else: ans.append('1')
    print(''.join(ans))
for _ in range(int(input())):
    solve()