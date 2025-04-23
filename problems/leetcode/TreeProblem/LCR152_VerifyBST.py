# https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
from typing import List
class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        """
        if we want a BST, then we need to have 3 segments
        postorder[st...end] + postorder[end + 1....j - 1] + postorder[j]
        postorder[j] is the root of our BST
        all values from postorder[st...end](inclusively) must be less than postorder[j]
        all values from postorder[end + 1...j - 1] must be greater than postorder[j]
        and postorder[st...end] and postorder[end + 1...j - 1] both of them must be BST as well
        otherwise it is not possible to be a BST 
        """
        def check(i: int, j: int) -> bool:
            # base case of recursion
            # whether empty or i == j which the tree right now only have a root
            # so it is true for both cases
            if i >= j: return True
            # we will find the first index such that postorder[i] > postorder[j]
            st = i
            while i < j and postorder[i] < postorder[j]:
                i += 1
            # we will then try to find the first index such that postorder[i] < postorder[j] after the first index of postorder[i] > postorder[j]
            st2 = i
            while i < j and postorder[i] > postorder[j]:
                i += 1
            # i must be reach j
            # and two parts must be a BST as well
            return i == j and check(st, st2 - 1) and check(st2, j - 1)
        return check(0, len(postorder) - 1)