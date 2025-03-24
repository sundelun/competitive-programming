from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        # nxt[i] represnt i pointing to the right-most position, initially nxt[i] = i + 1
        nxt = list(range(1, n))
        cur = n - 1
        # after adding an edge from l to r, if nxt[l] > r, it means we previously have an edge such that l' <= l < r <= r', so this edge is useless, we do nothing
        # otherwise, we point nxt[l] to r and mark all point [nxt[l]... r - 1] to r as well
        # the meanning of mark all points [nxt[l], r - 1] meanning they are being overlapped by a larger segments, each time we mark a new node, we reduce the cnt by 1
        for l, r in queries:
            while nxt[l] < r:
                cur -= 1
                nxt[l], l = r, nxt[l]
            ans.append(cur)
        return ans
        