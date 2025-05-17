# https://codeforces.com/contest/2061/problem/C
from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict, deque
from functools import cache
from typing import List
def solve():
    # if the i-th person is honest, there are a[i] liars to his left
    # if the i-th person is liar, then (i - 1)-th person must be honest
    # there are a[i - 1] number of liars to the left of (i - 1) person
    n = int(input())
    arr = [int(x) for x in input().split()]
    # add a zero at front
    arr = [0] + arr
    # f[i] represents number of arrangements with i-th person is honest
    # the answer is f[n] + f[n - 1](number of arragemnets with n'th person honest and (n - 1)'th person liar)
    f = [0] * (n + 1)
    mod = 998244353
    # empty people case with f[0] = 1
    f[0] = 1
    for i in range(1, n + 1):
        # if (i - 1) is honest, then arr[i] == arr[i - 1]
        if arr[i] == arr[i - 1]:
            f[i] = (f[i] + f[i - 1]) % mod
        # if (i - 1) is liar, then arr[i] == arr[i - 2] + 1
        # because i is honest, (i - 1) is liar, and (i - 2) is honest
        if i > 1 and arr[i] == arr[i - 2] + 1:
            f[i] = (f[i] + f[i - 2]) % mod
    print((f[n] + f[n - 1]) % mod)
for _ in range(int(input())):
    solve()