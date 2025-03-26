# https://leetcode.cn/problems/parsing-a-boolean-expression/
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for ch in expression:
            # do nothing here
            if ch == ",":
                continue
            # we first record all characters that are not right bracket
            if ch != ")":
                st.append(ch)
                continue
            # we will be counting the number of true and false from the expression a from (a)
            cnt_t = cnt_f = 0
            while st[-1] != "(":
                if st.pop() == "t":
                    cnt_t += 1
                else:
                    cnt_f += 1
            st.pop()
            sign = st.pop()
            # append result to top of the stack
            # if and then all expression/literal have to be true
            if sign == "&": st.append("t" if cnt_f == 0 else "f")
            # if or then one is true will be true
            elif sign == "|": st.append("t" if cnt_t else "f")
            # if not then do the reverse
            else: st.append("t" if cnt_t == 0 else "f")
        # at end the stack is guaranteed to be length of one, return the result based on stack
        return st[-1] == "t"