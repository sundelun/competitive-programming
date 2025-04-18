# https://leetcode.cn/problems/maximum-frequency-stack/
from collections import defaultdict
class FreqStack:
    def __init__(self):
        # the stack for each layer of number of occurence
        # for example if we first push [3, 4, 5] in order, then self.st = [[3, 4, 5]]
        # then if we push [4, 5, 6, 3] then self.st = [[3, 4, 5, 6], [4, 5, 3]]
        # so self.st[num_of_occur] is all elements occur num_of_occur number of times
        self.st = []
        # record of each val's number of occurence
        self.cnt = defaultdict(int)

    def push(self, val: int) -> None:
        # if number of occurence of val exceed the length of stack
        # then we need one more layer of stack
        if self.cnt[val] == len(self.st):
            self.st.append([val])
        # otherwise we append the value to the corresponding number of occurence level of stack
        else:
            self.st[self.cnt[val]].append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        # the most frequent element and most recent is self.st[-1][-1]
        ans = self.st[-1].pop()
        if not self.st[-1]: self.st.pop()
        self.cnt[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()