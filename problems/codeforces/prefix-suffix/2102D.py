from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
from collections import deque
# https://codeforces.com/contest/2106/problem/D
def solve():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    # same as subsequence matching
    suf = [m] * (n + 1)
    j = m
    # the list that satisfy the result is b[:j](prefix) + [ans] + b[j:](suffix)
    # where suf[j] is the suffix part's starting index 
    for i in range(n - 1, -1, -1):
        if a[i] >= b[j - 1]:
            j -= 1
        if j == 0:
            print(0)
            return
        suf[i] = j
    ans = math.inf
    # edge cases where we need to insert one element of value of b[0] at front to meet the requirements
    if suf[0] == 1: ans = b[0]
    j = 0
    # combine prefix and calc answer together
    for i in range(n):
        # if prefix we have a match
        # we add prefix part's ending index(excluded) by 1
        if a[i] >= b[j]:
            j += 1
        # if it is now enough to make have inserted one value that match satisfy the answer
        if suf[i + 1] <= j + 1:
            ans = min(ans, b[j])
    print(ans) if ans < math.inf else print(-1)
for _ in range(int(input())):
    solve()