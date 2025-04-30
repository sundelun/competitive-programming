# https://leetcode.cn/problems/find-the-lexicographically-smallest-valid-sequence/description/
from typing import List
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        # similar to question 2565
        n, m = len(word1), len(word2)
        j = m
        # same as find subsequence by iterating in reverse order
        # 
        suf = [m] * (n + 1)
        for i in range(n - 1, -1, -1):
            if j and word1[i] == word2[j - 1]:
                j -= 1
            suf[i] = j
        ans = []
        # greedy stragedy
        # if s[i] == t[j]: then it means a matching we should include it into answer since wea re finding the smallest
        # if s[i] != t[j] and suf[i + 1] <= j + 1 it means after chaning s[i] to t[j]
        # t[j + 1:] is the subsequence of s[i + 1:] because it means the suffix part of s[i:]'s starting index is less than or equal to the starting index of t[j + 1](= j + 1)
        # we must make the change here because otherwise the answer is not the smallest answer
        j = 0
        changed = False
        for i, c in enumerate(word1):
            if c == word2[j] or not changed and suf[i + 1] <= j + 1:
                if c != word2[j]:
                    changed = True
                ans.append(i)
                j += 1
                if j == m: return ans
        return []