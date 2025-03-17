# https://leetcode.cn/problems/word-search/description/
from typing import List
from collections import Counter
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # optimization
        cnt = Counter(c for row in board for c in row)
        # if there are not enough board's character for word
        if cnt < Counter(word): return False 
        # if the last character's occurence is less than first character's occurence
        # then we would start from the last character to make less number of backtrack!
        if cnt[word[-1]] < cnt[word[0]]: word = word[::-1]
        m, n = len(board), len(board[0])
        length = len(word)
        def dfs(x: int, y: int, i: int) -> bool:
            # if found, return True
            if i == length: return True
            # mark board[x][y] as visited
            tmp, board[x][y] = board[x][y], '#'
            res = False
            # traverse all directions
            for dx, dy in DIRS:
                if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] == word[i]:
                    res = res or dfs(x + dx, y + dy, i + 1)
            # recover
            board[x][y] = tmp
            return res
        for i in range(m):
            for j in range(n):
                # I will only start dfs if the first character match
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True
        return False

