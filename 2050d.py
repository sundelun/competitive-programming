from itertools import accumulate
import math
import bisect
import heapq
def solve():
    s = str(input())
    n = len(s)
    arr = [int(ch) for ch in s]
    left = []
    for i in range(n):
        left.append([max(0, i - arr[i]), i, arr[i]])
    left.sort(key = lambda x: x[0])
    print(left)
    h = []
    ans = [-1] * n
    p = 0
    for i in range(n):
        while p < n and left[p][0] == i:
            _, j, d = left[p]
            key = d + min(0, (i - j))
            heapq.heappush(h, (-key, j, d))
            p += 1
        print(h)
        if h:
            key, j, d = heapq.heappop(h)
            val = d + min(0, i - j)
            if val < 0: val = 0
            ans[i] = val
        else:
            ans[i] = 0
    print(''.join(map(str, ans)))
for _ in range(int(input())):            
    solve()