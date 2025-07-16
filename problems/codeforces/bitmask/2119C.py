from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
from collections import deque
def solve():
    n, l, r, k = map(int, input().split())
    if n == 2:
        print(-1)
        return
    if n % 2:
        print(l)
        return
    # if n is odd then the answer is [l] * n
    # if n = 2, then the only valid solution is [0, 0] but l >= 1 so no solution when n = 2
    # so if n is even, we cannot just set arr = [l] * (n - 1) and just change an
    # we will try to make a1 = a2 = ... = a(n - 3) = l
    # then we observe if l's any bit is 1, we will make the last two number bit 0; and if any l's bit is 0 we will make last two number bit 0 as well
    # finally add a bit 1 to front to make it smallest
    cnt = l.bit_length()
    val = pow(2, cnt)
    if val > r:
        print(-1)
        return
    print(l) if k < n - 1 else print(val)
for _ in range(int(input())):
    solve()