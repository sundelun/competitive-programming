# https://leetcode.cn/problems/sliding-window-median/description/
from collections import defaultdict
import heapq
from typing import List
class LazyHeap:
    def __init__(self):
        self.heap = []
        # record the how many times an element should be removed
        self.remove_cnt = defaultdict(int)
        # the size of the heap
        self.size = 0

    def remove(self, num: int) -> None:
        # remove the element num from the heap
        self.remove_cnt[num] += 1
        self.size -= 1
    
    def applyremove(self) -> None:
        # make sure the heap's top element is the "real" element
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1
            heapq.heappop(self.heap)

    def top(self) -> int:
        # query the top element
        self.applyremove()
        return self.heap[0]

    def pop(self) -> int:
        # same operation as heappop
        self.applyremove()
        self.size -= 1
        return heapq.heappop(self.heap)

    def push(self, num: int) -> None:
        # if there is num to be removed, we do not heappush
        if self.remove_cnt[num] > 0:
            self.remove_cnt[num] -= 1
        else:
            heapq.heappush(self.heap, num)
        self.size += 1
    
    def pushpop(self, num: int) -> int:
        # first push(num) to heap then pop
        self.applyremove()
        heapq.heappush(self.heap, num)
        val = heapq.heappop(self.heap)
        return val

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = LazyHeap() # the heap that record first half of window
        right = LazyHeap() # the heap that record second half of window
        ans = []
        for i, num in enumerate(nums):
            if left.size == right.size:
                # similar to question #295, push based on size of two heaps
                left.push(-right.pushpop(num))
            else:
                right.push(-left.pushpop(-num))
            if i < k - 1: continue
            # also similar to 295 decide which heap to inserted
            if k % 2:
                ans.append(-left.top())
            else:
                ans.append((-left.top() + right.top()) / 2.0)
            leave_num = nums[i - k + 1]
            # if the popping element is less than or equal to biggest element in left, then the deleted element must be in left
            if leave_num <= -left.top():
                left.remove(-leave_num)
                # adjust the size of heap if needed
                if left.size < right.size:
                    left.push(-right.pop())
            else:
                right.remove(leave_num)
                if left.size > right.size + 1:
                    right.push(-left.pop())
        return ans