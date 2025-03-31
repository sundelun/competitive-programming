# https://leetcode.cn/problems/odd-even-linked-list/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        evenhead = head.next
        odd, even = head, evenhead
        # odd and even always separeate by one node
        while even and even.next:
            odd.next = even.next # assignt odd.next with even.next
            odd = odd.next # odd go to the next
            even.next = even.next.next # assign even.next
            even = even.next # even go to the next
        # odd's tail next assign with even's head
        odd.next = evenhead
        return head
