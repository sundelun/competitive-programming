# https://codeforces.com/contest/2110/problem/C
from itertools import accumulate, pairwise
import math
import bisect
import heapq
from collections import Counter, defaultdict, deque
from functools import cache
from typing import List
def solve():
   n = int(input())
   arr = [int(x) for x in input().split()]
   left = [-1] * n
   right = [-1] * n
   for i in range(n):
      l, r = map(int, input().split())
      left[i] = l
      right[i] = r
   # the question requires l_i <= h_i <= r_i
   l = 0
   # st to record all -1's index(able to switch index)
   # we will also maintain the lower and upper bound
   # lower bound = l; upper bound = l + len(st)
   # we require l_i <= h_i, so if we make all unknown as 0, then h_i = l
   # if lower_bound < left[i] then we must make some unknown index to 1
   # symmetrically, we require h_i <= r_i, if we make all unknow as 1, then h_i = l + len(st)
   # if l + len(st) > r_i, then we must make some unknown to 0
   st = []
   for i in range(n):
      if arr[i] == -1:
         st.append(i)
      else:
         l += arr[i]
      while l < left[i]:
         if not st:
            print(-1)
            return
         arr[st.pop()] = 1
         l += 1
      while l + len(st) > right[i]:
         if not st:
            print(-1)
            return
         arr[st.pop()] = 0
   for i in range(n):
      arr[i] = max(0, arr[i])
   print(" ".join(map(str, arr)))
for _ in range(int(input())):
   solve()