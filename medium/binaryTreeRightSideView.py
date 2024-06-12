# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        levels, ans = {}, []
        def traverse(node, level):
            if node is None:
                return
            if level not in levels.keys():
                levels[level] = []
            levels[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        
        traverse(root, 0)

        for row in levels.values():
            ans.append(row.pop())
        
        return ans

sol, root = Solution(), TreeNode()
root.left = TreeNode()
root.right = TreeNode()
root.val = 1

root.right.val = 3
root.left.val = 2

root.left.right = TreeNode()
root.left.right.val = 4

print(sol.rightSideView(root))
