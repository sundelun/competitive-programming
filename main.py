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
@cache
def calc(x: int, a: int, b: int) -> int:
    if x == 0: return 0
    if a == 0 and b == 0: return x
    if x == 1: return 0 if a > 0 else 1
    if x & 1 == 0:
        return max((calc(x >> 1, a - 1, b) if a > 0 else -math.inf), ((calc(x >> 1, a, b - 1) if b > 0 else -math.inf)))
    return max((calc(x >> 1, a - 1, b) if a > 0 else -math.inf), ((calc((x + 1) >> 1, a, b - 1) if b > 0 else -math.inf)))
@cache
def calc2(x: int, a: int, b: int) -> int:
    if x == 0: return 0
    if a == 0 and b == 0: return x
    if x == 1: return 0 if a > 0 else 1
    if x & 1 == 0:
        return min((calc2(x >> 1, a - 1, b) if a > 0 else math.inf), ((calc2(x >> 1, a, b - 1) if b > 0 else math.inf)))
    return min((calc2(x >> 1, a - 1, b) if a > 0 else math.inf), ((calc2((x + 1) >> 1, a, b - 1) if b > 0 else math.inf)))
def solve():
    x, m, n = map(int, input().split())
    # 3 1 2
    # big: 3 -> 2 -> 1 -> 1
    print(calc2(x, m, n), calc(x, m, n))
for _ in range(int(input())):
    solve()