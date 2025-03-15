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
    x2, n2, m2 = map(int, input().split())
    n, m = n2, m2
    x = x2
    while x > 1:
        if n == 0 and m == 0: break
        if x & 1:
            if m: 
                x >>= 1
                x += 1
                m -= 1
            else:
                x >>= 1
                n -= 1
        else:
            x >>= 1
            if n: n -= 1
            else: m -= 1
    if n and x == 1: x = 0
    #rint(x)
    x1 = x2
    n1, m1 = n2, m2
    while x1:
        if n1 == 0 and m1 == 0: break
        if x1 & 1 == 0:
            x1 >>= 1
            if m1: 
                m1 -= 1
            else:
                n1 -= 1
        else:
            x1 >>= 1
            if n1: 
                n1 -= 1
            else:
                m1 -= 1
                x1 += 1
    print(x1, x)
for _ in range(int(input())):
    solve()