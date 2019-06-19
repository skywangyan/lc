'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
 key.
The right subtree of a node contains only nodes with keys greater than the
 node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        def preOrder(node):
            if not node:
                return
            preOrder(node.left)
            res.append(node.val)
            preOrder(node.right)
        preOrder(root)
        prev = None
        for i in res:
            if prev is None:
                prev = i
                continue
            if i <= prev:
                return False
            else:
                prev = i
        else:
            return True
s = Solution()
a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
a.left, a.right = b, c
print s.isValidBST(a)