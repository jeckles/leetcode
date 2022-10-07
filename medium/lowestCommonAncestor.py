# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        goRight, goLeft, level, minNode = False, False, 0, None
        if self.exists(p, root) and self.exists(q, root):
            level, minNode = self.__lowestCommonAncestor(root, p, q, level)
                
    def __lowestCommonAncestor(self, node, p, q, prevLevel):
        leftLevel, rightLevel, leftMinNode, rightMinNode = -1, -1, TreeNode(-1), TreeNode(-1)
        if node is None:
            return (-1, None)
        if self.exists(p, node.left) and self.exists(q, node.left):
           (leftLevel, leftMinNode) = self.__lowestCommonAncestor(node.left, p, q, level += 1)
        if self.exists(p, node.right) and self.exists(q, node.right):
            (rightLevel, rightMinNode) = self.__lowestCommonAncestor(node.right, p, q, level += 1)
        if leftLevel > rightLevel:
            return (leftLevel, leftMinNode)
        else:
            return (rightLevel, rightMinNode)
                
    def exists(self, find, node):
        if node is None:
            return False
        if node.val == find:
            return True
        else:
            checkLeft = self.exists(find, node.left)
            checkRight = self.exists(find, node.right)
            return (checkLeft or checkRight)
