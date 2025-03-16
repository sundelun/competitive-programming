from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
from collections import deque
# https://codeforces.com/contest/2078/problem/C
def solve():
    n = int(input())
    arrb = [int(x) for x in input().split()]
    arrb.sort()
    s = 0
    ans = [arrb[-1]]
    """
    a1 = a2 - a3 + a4 - a5 + ..... + x - a0
    sort the array a
    a2n = a2 + a3 + .... an-1 + an - an+1....an+2 + x - a1  
    x = a2n + a1 - a2 - a3 - ....-an-1 - an + an+1 + an+2.....+a2n-1
    we put arrb[-1](a[2n]) as a1, now for rest (n - 1) * 2 number we put +a[i] and a[i + n - 1] to make sure the calculate s is negative
    for second last element we put s + arr[-1] + arr[0] to make sure s is distinct from every element(biggest one) and arrb[0] as last one
    """
    for i in range(1, n):
        ans.append(arrb[i])
        ans.append(arrb[i + n - 1])
        s += arrb[i + n - 1] - arrb[i]
    # x = a2n + a1 - a2 - a3 - ....-an-1 - an + an+1 + an+2.....+a2n-1
    ans.append(s + arrb[-1] + arrb[0])
    ans.append(arrb[0])
    print(" ".join(map(str, ans)))
for _ in range(int(input())):
    solve()