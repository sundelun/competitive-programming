from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
from collections import deque
def solve():
    n, m = map(int, input().split())
    s = str(input())
    t = str(input())
    suf = [n] * m
    i = n - 1
    # suf[j] represents the maximum index i that satisfy t[j] = s[i]
    for j in range(m - 1, -1, -1):
        while t[j] != s[i]:
            i -= 1
        suf[j] = i
        i -= 1
    pre = [0] * m
    i = 0
    # pre[j] represents the minimum index i that satisfy t[j] = s[i]
    for j in range(m):
        while t[j] != s[i]:
            i += 1
        pre[j] = i
        i += 1
    ans = 0
    # so the answer will be max(suf[i + 1] - pre[i], pre[i + 1] - pre[i], suf[i + 1] - suf[i])
    for i in range(m - 1):
        ans = max(ans, suf[i + 1] - pre[i], pre[i + 1] - pre[i], suf[i + 1] - suf[i])
    print(ans)
#for _ in range(int(input())):
solve()