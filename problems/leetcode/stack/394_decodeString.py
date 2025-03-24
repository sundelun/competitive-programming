# https://leetcode.cn/problems/decode-string/description/
"""
The key solution is use a stack to maintain the calculation
I use a recursion method here to do calculation with bracket result
"""
class Solution:
    # find the matching closing bracket with respect to bracket at index i
    def findindex(self, s: str, st: int) -> int:
        cnt = 1
        for j in range(st, len(s)):
            if s[j] == ']':
                cnt -= 1
            elif s[j] == '[':
                cnt += 1
            if cnt == 0:
                return j
    def decodeString(self, s: str) -> str:
        ans = []
        i = 0
        n = len(s)
        num = 1
        while i < n:
            if s[i] == '[':
                # first find the matching closing bracket
                j = self.findindex(s, i + 1)
                # calculate the result of the expression of a coming from [a]
                tmp = self.decodeString(s[i + 1: j])
                # append to answer
                ans.append(num * tmp)
                # we need to reset the number of times to 1
                num = 1
                i = j + 1
            elif s[i].isdigit():
                # calculate the new number of times to be multiplied
                newnum = 0
                while s[i].isdigit():
                    newnum = newnum * 10 + int(s[i])
                    i += 1
                num = newnum
            else:
                # otherwise we just record the wanted alpha
                tmp = []
                while i < len(s) and s[i].isalpha():
                    tmp.append(s[i])
                    i += 1
                # add to answer and reset num to 1 again
                tmp = tmp * num
                ans.append(''.join(tmp))
                num = 1
        return ''.join(ans)
                