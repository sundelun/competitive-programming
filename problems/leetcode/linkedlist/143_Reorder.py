# https://leetcode.cn/problems/reorder-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # the function that reverse a linked list
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            cur = head
            prev = None
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        # find the mid point of a linked list using slow fast pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        # now head is equal to first half of linked list(including the mid node)
        # head2 is equal to second half of linked list in the reversing order(also including the mid node)
        # then reconstruct the linked list
        head2 = reverse(temp)
        # we use head2.next to be ending condition because both head and head2 have mid node as ending
        # if we use head2 it will be an extra node pointing to itself
        while head2.next:
            nxth = head.next
            nxth2 = head2.next
            head.next = head2
            head2.next = nxth
            head = nxth
            head2 = nxth2