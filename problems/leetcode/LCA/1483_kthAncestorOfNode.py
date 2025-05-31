# https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/description/
from typing import List
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # we will precompute each node's pow(2, i)'s parent node
        # because each positve integer can be represented in binary format, for example 13 = 1 + 4 + 8
        # we can reach each node's k'th ancestor node in time complexity of O(logK)
        # pa[i][j] means node i's j'th parent
        # for example pa[x][0] means x's parent node, while pa[x][1] = pa[pa[x][0]][0](x's grandfather node)
        # and pa[x][2] = pa[pa[x][1]][0]...etc
        # pa[x][i + 1] = pa[pa[x][i]][i] (means pow(2, i + 1) is parent of pow(2, i))
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                if pa[x][i] != -1:
                    pa[x][i + 1] = pa[pa[x][i]][i]
        self.pa = pa
    # get the k'th ancesor of a node
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            # if k's i-th bit is one, we move to its parent
            if (k >> i) & 1:
                node = self.pa[node][i]
                if node < 0: break
        return node

