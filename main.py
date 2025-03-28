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
    arr = [int(x) for x in input().split()]
    f = [[0] * 2 for _ in range(n)]
    # f[i][0] represents ending with a[i]'s longest increasing subarray
    # f[i][1] represents we have changed one element that ending with a[i]'s longest increasing subarray
    # 2 3 5 1
    f[0][0] = f[0][1] = 1
    ans = 1
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            f[i][0] = f[i - 1][0] + 1
            f[i][1] = f[i - 1][1] + 1
        else:
            # f[i][0] can only be 1
            f[i][0] = 1
            # by changing a[i - 1] to a very small number
            f[i][1] = 2
        # by changing a[i - 1] such that a[i] > a[i - 1] > a[i - 2]
        if i > 1 and arr[i] > arr[i - 2] + 1:
            f[i][1] = max(f[i][1], f[i - 2][0] + 2)
        ans = max(ans, f[i][0], f[i][1], f[i - 1][0] + 1)
    print(ans)
#for _ in range(int(input())):
solve()