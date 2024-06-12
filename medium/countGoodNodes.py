# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, maxVal):
            if node == None:
                return 0
            elif node.val <= maxVal:
                countL = traverse(node.left, max(maxVal, node.val))
                countR = traverse(node.right, max(maxVal, node.val))
                return countL + countR + 1
            else:
                countL = traverse(node.left, max(maxVal, node.val))
                countR = traverse(node.right, max(maxVal, node.val))
                return countL + countR
        return traverse(root, -1) + 1

sol, root = Solution(), TreeNode()
root.left = TreeNode()
root.right = TreeNode()
root.val = 3

root.left.val = 4

root.right.val = 6

root.left.left = TreeNode()
root.left.left.val = 5

root.right.right = TreeNode()
root.right.right.val = 2

root.left.left.left = TreeNode()
root.left.left.left.val = 2

root.right.right.right = TreeNode()
root.right.right.right.val = 5

print(sol.goodNodes(root))