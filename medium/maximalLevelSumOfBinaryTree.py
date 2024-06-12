# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = {}

        def traverse(node, lvl):
            if node is None:
                return
            if lvl not in level.keys():
                level[lvl] = node.val
                traverse(node.left, lvl + 1)
                traverse(node.right, lvl + 1)
            else:
                level[lvl] += node.val
                traverse(node.left, lvl + 1)
                traverse(node.right, lvl + 1)
        traverse(root, 0)
        return level

sol, root = Solution(), TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(5, None, None))
print(sol.maxLevelSum(root))