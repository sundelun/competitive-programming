# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/description/
from typing import List
from collections import deque
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        # as i decrease, the windows of [i + 1, 2 * i + 1] is also decreasing
        # so we can solve it by using a monotonic queue
        # q is in decreasing order in cost and increasing in index
        n = len(prices)
        q = deque()
        q.append((n + 1, 0))
        for i in range(n, 0, -1):
            # by purchase fruits[i], cannot satisfy free of q[-1][0]
            while q[-1][0] > i * 2 + 1:
                q.pop()
            # f is the cost by choosing to buy fruits[i....n]
            f = prices[i - 1] + q[-1][1]
            # while choosing to buy fruits[i] is more optimal than buying q[0][0]
            while q and f <= q[0][1]:
                q.popleft()
            # append to the deque of buying fruits[i]'s cost and index
            q.appendleft((i, f))
        # the answer is the cost of purchase fruits[0..n]
        return q[0][1]