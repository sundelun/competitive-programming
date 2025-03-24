# 224 Basic Calculator: https://leetcode.cn/problems/basic-calculator/description/
# 227 Basic Calculator II: https://leetcode.cn/problems/basic-calculator-ii/description/
# 772 Basic Calculator III: https://leetcode.cn/problems/basic-calculator-iii/description/
# the previous two version works with 3rd version, only provide 3rd version here
"""
The key idea is to use a stack maintain all results of calculation
And use a recursion method to do calculation with bracket
"""
class Solution:
    def calculate(self, s: str) -> int:
        # find the matching closing bracket with respect to bracket at index i
        def close(s: str, i: int) -> int:
            level = 1
            st = i
            while st < n and level != 0:
                if s[st] == '(': level += 1
                elif s[st] == ')': level -= 1
                st += 1
            # s[st - 1] == ')'
            return st - 1
        i = 0
        n = len(s)
        st = []
        # the previous symbol
        op = "+"
        num = 0
        while i < n:
            # accumulate digit number
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            # if we find a bracket, then use recursion to calculate the expression [a]'s result a
            if s[i] == '(':
                j = close(s, i + 1)
                num = self.calculate(s[i + 1: j])
                i = j
            # If we find a calc symbol or at end of expression, we record it to answer
            if s[i] in "+-*/" or i == n - 1:
                # for plus and minus just append to stack
                if op == '+':
                    st.append(num)
                elif op == '-':
                    st.append(-num)
                # for multiply and divide we use the result from top-stack
                elif op == '*':
                    st.append(st.pop() * num)
                else:
                    st.append(int(st.pop() / num))
                num = 0
                #update the latest operation sign
                op = s[i]
            i += 1
        # the answer is the sum of stack
        return sum(st)