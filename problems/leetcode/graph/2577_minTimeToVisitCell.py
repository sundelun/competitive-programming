# https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/
from typing import List
import heapq
import math
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # the general idea of this question is if grid[1][0] and grid[0][1] > 1 then we cannot reach bottom-right
        # otherwise we can reach any grid position by jumping back-and-forth
        # so the solution is identical to Dijkstra-algo
        
        # case where we cannot reach the bottom-right
        if grid[0][1] > 1 and grid[1][0] > 1: return -1

        # Dijkstra-algo with small modification
        m, n = len(grid), len(grid[0])
        record = [[math.inf] * n for _ in range(m)]
        record[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            time, x, y = heapq.heappop(h)
            if x == m - 1 and y == n - 1:
                return time
            if time > record[x][y]: continue
            for dx, dy in DIRS:
                newx = x + dx
                newy = y + dy
                st = time
                if 0 <= newx < m and 0 <= newy < n:
                    # (((grid[newx][newy] - st) % 2) == 0) this part for we have to reach the grid by one more move
                    # for example if we have grid = [[0, 0], [0, 5]] then our solution is 6 because at time 4 we cannot reach bottom-right
                    end = max(st + 1, grid[newx][newy] + (((grid[newx][newy] - st) % 2) == 0))
                    if end < record[newx][newy]:
                        record[newx][newy] = end
                        heapq.heappush(h, (end, newx, newy))