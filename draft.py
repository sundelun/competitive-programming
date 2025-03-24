from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict
from functools import cache
from typing import List
import sys

class SegmentTree:
    def __init__(self, arr):
        """
        Build a Segment Tree for the array 'arr'.
        Each node stores the maximum value in its segment.
        """
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        
        self.tree = [0] * (2 * self.size)
        
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])
    
    def update(self, pos: int, new_val: int) -> None:
        pos += self.size
        self.tree[pos] = new_val
        
        pos >>= 1
        while pos >= 1:
            self.tree[pos] = max(self.tree[pos << 1], self.tree[pos << 1 | 1])
            pos >>= 1
    
    def get_leftmost_index(self, val):
        """
        Find the leftmost index i such that tree[i] >= val.
        Returns -1 if no such basket exists.
        
        We check the root: if it's < val, no basket can hold val.
        Otherwise, we descend from the root to find the leftmost
        position in a leaf that satisfies tree[leaf] >= val.
        """
        # Root index is 1. If max in entire range < val, return -1.
        if self.tree[1] < val:
            return -1
        
        idx = 1
        while idx < self.size:
            left_child = idx << 1
            right_child = left_child | 1
            if self.tree[left_child] >= val:
                idx = left_child
            else:
                idx = right_child
        
        return idx - self.size


def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    fruits = list(map(int, data[1 : 1 + n]))
    baskets = list(map(int, data[1 + n : 1 + 2*n]))
    
    # Build the segment tree with the basket capacities
    seg = SegmentTree(baskets)
    
    unplaced = 0
    
    # For each fruit, find the leftmost valid basket
    for fruit_qty in fruits:
        pos = seg.get_leftmost_index(fruit_qty)
        if pos == -1:
            # No basket can hold this fruit
            unplaced += 1
        else:
            # Mark this basket as used by setting its capacity to -1
            seg.update(pos, -1)
    
    print(unplaced)


if __name__ == "__main__":
    # Example usage:
    # Input format (as in the original problem statement):
    # n
    # fruits[0] fruits[1] ... fruits[n-1]
    # baskets[0] baskets[1] ... baskets[n-1]
    #
    # Then run: python3 your_file.py < input.txt
    #
    # This solve() function will parse the input, compute, and print the result.
    solve()
def solve():
    n, q = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    mod = 998244353
    # a = [1, 4] and b = [2, 3] then the max of min is 1 * 3 = 3
    # greedy approach: the optimal answer is sort a and sort b and simulate will give the answer!
    a.sort()
    b.sort()
    res = 1
    for i in range(n):
        res = ((res % mod )* (min(a[i], b[i])) % mod) % mod
    ans = [res]
    # [4, 5, 6] and a[0] += 1
    # [1, 1, 1] original res = 1
    # after b[0] += 1, it becomes 2
    for _ in range(q):
        o, x = map(int, input().split())
        original = min(a[x - 1], b[x - 1])
        # a * (b + 1) = a * b + a
        # b = original, a = updated res
        res //= original
        if o == 1:
            if a[x - 1] < b[x - 1]:
                res = res * (original + 1)
            else:
                res *= original
            a[x - 1] += 1
        else:
            if a[x - 1] > b[x - 1]:
                res = res * (original + 1)
            else:
                res *= original
            b[x - 1] += 1
        ans.append(res % mod)
    print(ans)
for _ in range(int(input())):
    solve()