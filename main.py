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
    x, y = map(int, input().split())
    # (x + k) + (y + k) = (x + k) xor (y + k) is equivalant to (x + k) and (y + k) = 0
    # a number that is a power of 2 does not share any digits with number that is less than him
    # if x == y then no possible k value
    if x == y:
        print(-1)
        return
    if x & y == 0:
        print(0)
        return
    # to make x < y
    if x > y:
        x, y = y, x
    st = 1
    while st <= y:
        st <<= 1
    # the answer to k is 2 ** n - max(x, y)
    print(st - y)
for _ in range(int(input())):
    solve()