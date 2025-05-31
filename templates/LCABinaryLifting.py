from typing import List
class LcaBinaryLifiting:
    def __init__(self, edges: List[List[int]]):
        # edges means there is an undirected edge between x and y
        n = len(edges) + 1
        m = n.bit_length()
        # first construct the graph
        g = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            g[x].append(y)
            g[y].append(x)
        
        # the depth of each node
        depth = [0] * n
        # we will precompute each node's pow(2, i)'s parent node
        # because each positve integer can be represented in binary format, for example 13 = 1 + 4 + 8
        # we can reach each node's k'th ancestor node in time complexity of O(logK)
        # pa[i][j] means node i's j'th parent
        # for example pa[x][0] means x's parent node, while pa[x][1] = pa[pa[x][0]][0](x's grandfather node)
        # and pa[x][2] = pa[pa[x][1]][0]...etc
        # pa[x][i + 1] = pa[pa[x][i]][i] (means pow(2, i + 1) is parent of pow(2, i))
        pa = [[-1] * m for _ in range(n)]
        # first record all node's father by dfs
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)
        dfs(0, -1)
        
        # then we will be recording all further level of parent
        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    # get the k'th ancesor of a node
    def get_kth_ancestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            # if k's i-th bit is one, we move to its parent
            if k >> i & 1:
                node = self.pa[node][i]
        return node

    # get the lca node of node x and node y
    def get_lca(self, x: int, y: int) -> int:
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # make x and y at same level of depth
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        # it means the lca node is x
        if y == x: return x
        # otherwise jump up at same time for node x and node y
        # if node x's pow(2, i) ancestor node does not exsist(pa[x][i] = -1) then we decrease i by one
        # otherwise if they exsist, and pa[x][i] != pa[y][i], the lca is stil above, we move both x and y one level up
        # if pa[x][i] == pa[y][i], then lca might be below x, we will decrease i by one
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py
        # the lca is x's parent node
        return self.pa[x][0]

    # the distance between node x and node y
    def get_dis(self, x: int, y: int) -> int:
        return self.depth[x] + self.depth[y] - self.depth[self.get_lca(x, y)] * 2