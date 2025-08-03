"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""    

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Рекурсивно находим глубину левого и правого поддеревьев
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Глубина текущего узла = 1 (сам узел) + максимальная из глубин поддеревьев
        return 1 + max(left_depth, right_depth)

