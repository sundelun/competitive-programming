from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
from collections import deque

class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.fw = [0] * (n + 1) # by using index(1-indexed) from 1 to n
        pw = 1
        # Precompute the largest power of two ≤ n, to accelerate find_kth
        while pw <= n:
            pw <<= 1
        self._top = pw >> 1 # highest power of two ≤ n

    # a[i](0-indexd for input-parameter) add delta, O(logN)
    def update(self, i: int, delta: int):
        # changed to 1-indexed
        i += 1
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i
    
    # calculate the prefix sum of a[0] + a[1] + .. +a[i] (0-indexed for input-paramater), O(logN)
    def prefix(self, i: int) -> int:
        # change to 1-indexed
        i += 1
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    
    # calculate the inerval sum of a[l] + a[l + 1] .... + a[r] (0-indexed for input-paramater), O(logN)
    def query(self, l: int, r: int) -> int:
        if r < l:
            return 0
        return self.prefix(r) - self.prefix(l - 1)

    # return the sum over a[0...n - 1]
    def total(self) -> int:
        return self.prefix(self.n - 1)
    
    # Return the smallest index i (0-based) such that sum[0..i] >= k.
    def find_kth(self, k: int) -> int:
        idx = 0
        bit_mask = self._top
        while bit_mask > 0:
            t = idx + bit_mask
            if t <= self.n and self.fw[t] < k:
                idx = t
                k -= self.fw[t]
            bit_mask >>= 1
        # The desired Fenwick index is idx+1, so the 0-based position is (idx).
        return idx

def solve():
    n, q = map(int, input().split())
    # we only care about 5 conditions that can make string smaller
    # 1. b -> a
    # 2. b -> c -> a
    # 3. c -> a
    # 4. c -> b
    # 5. c -> b -> a
    s = list(input())
    # create a 2d list with a Fenwick Tree inside each elemet
    # record[x][y] stores a Fenwick Tree that store all index of query that change from x -> y
    record = [[FenwickTree(q) for _ in range(3)] for _ in range(3)]
    for i in range(q):
        a, b = map(str, input().split())
        a = ord(a) - ord('a')
        b = ord(b) - ord('a')
        # add one to fenwick tree with corresponding query
        record[a][b].update(i, 1)
    for i in range(n):
        if s[i] == 'b':
            # if we have an available b -> a
            if record[1][0].total() > 0:
                # find the smallest index that have b -> a and update the Fenwick Tree
                idx = record[1][0].find_kth(1)
                record[1][0].update(idx, -1)
                s[i] = 'a'
            # if we have an available b -> c
            elif record[1][2].total() > 0:
                # find the smallest index that have b -> c
                idx = record[1][2].find_kth(1)
                # number of index of c -> a that is before the first available b -> c
                cnt = record[2][0].prefix(idx - 1)
                tot = record[2][0].total()
                # if we have some available index of c -> a that is after first available b -> c
                if cnt < tot:
                    # update both fenwick tree
                    record[1][2].update(idx, -1)
                    # find the first index of (c -> a) after first (b -> c)
                    idx2 = record[2][0].find_kth(cnt + 1)
                    record[2][0].update(idx2, -1)
                    s[i] = 'a'
        elif s[i] == 'c':
            # if we have an available c -> a
            if record[2][0].total() > 0:
                idx = record[2][0].find_kth(1)
                record[2][0].update(idx, -1)
                s[i] = 'a'
            # if we have an available c -> b
            elif record[2][1].total() > 0:
                # find the smallest index that have c -> b
                idx = record[2][1].find_kth(1)
                # number of index of b -> a that is before the first available c -> b
                cnt = record[1][0].prefix(idx - 1)
                tot = record[1][0].total()
                # if we have some available index of b -> a that is after first available c -> b
                if cnt < tot:
                    # find the first index of (b -> a) after first (c -> b)
                    idx2 = record[1][0].find_kth(cnt + 1)
                    record[1][0].update(idx2, -1)
                    s[i] = 'a'
                # otherwise we will do a c -> b
                else:
                    s[i] = 'b'
                record[2][1].update(idx, -1)

    print("".join(s))
for _ in range(int(input())):
    solve()