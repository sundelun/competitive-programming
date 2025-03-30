# https://leetcode.cn/problems/find-median-from-data-stream/description/
import heapq
class MedianFinder:
    # the key idea is to maintain two heap one with min-heap and second with max-heap
    # the size of two heaps always differ no more than one
    def __init__(self):
        self.left = [] # store the first half of array in sorted order
        self.right = [] # stored the second half of array in sorted order

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            # then we push the new element to first half or array
            heapq.heappush(self.right, num)
            heapq.heappush(self.left, -heapq.heappop(self.right))
        else:
            # otherwise we push to the second half of array
            heapq.heappush(self.left, -num)
            heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        # return the median with both odd and even cases
        # if left size is same as right size then the length is even
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        return -self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()