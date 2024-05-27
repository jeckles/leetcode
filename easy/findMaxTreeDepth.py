# Definition for a binary tree node.
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def __init__(self) -> None:
        pass
    
    def maxDepthHelper(self, node, level) -> int:
        if node is None:
            return level
        else:
            return max(self.maxDepthHelper(node.left, level + 1), self.maxDepthHelper(node.right, level + 1))
        
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepthHelper(root.left, 1), self.maxDepthHelper(root.right, 1))
        
s, n = Solution(), TreeNode(0, TreeNode(1, TreeNode(2, None, None), TreeNode(3, TreeNode(4), None)), None)
maxDepth = s.maxDepth(n)

print(maxDepth)