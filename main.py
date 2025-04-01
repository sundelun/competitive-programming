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
    s = str(input())
    # TI -> TLI -> TILI -> TILTI if there is one pair that could be operate then we can have a solution!
    # TILII cntT = 1, cntL = 1, cntI = 3
    # ILLL -> ITLLL -> ITILLL -> ITITLLL -> ITITILLL -> ITITITLLL
    # LLI -> LLTI -> LLITI -> LLTITI
    cntT = cntL = cntI = 0
    for ch in s:
        if ch == "T": cntT += 1
        elif ch == "L": cntL += 1
        else: cntI += 1
    if cntT == cntI == cntL:
        print(0)
        return
    mx = max(cntT, cntI, cntL)
    if cntT == mx: mxch = "T"
    elif cntI == mx: mxch = "I"
    else: mxch = "L"
    if cntT + cntI + cntL - mx == 0:
        print(-1)
        return
    ans = mx * 3 - n
    print(ans)
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            if s[i] == mxch:
                for _ in range(ans):
                    print(i + 1)
            else:
                for j in range(ans):
                    print(i + j + 1)
            return
for _ in range(int(input())):
    solve()