'''
    
                3
            /       \
        5               1
    /       \       /       \
   2         4     6         7
    
    p = 2, q = 4
    
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        level, minNode = 0, None
        if self.exists(p, root) and self.exists(q, root):
            level, minNode = self.__lowestCommonAncestor(root, p, q, level)
        return minNode.val
                
    def __lowestCommonAncestor(self, node, p, q, prevLevel):
        leftLevel, rightLevel, leftMinNode, rightMinNode = -1, -1, TreeNode(-1, None, None), TreeNode(-1, None, None)
        if node is None:
            return (-1, None)
        if self.exists(p, node.left) and self.exists(q, node.left):
            prevLevel += 1
            leftLevel, leftMinNode = self.__lowestCommonAncestor(node.left, p, q, prevLevel)
        if self.exists(p, node.right) and self.exists(q, node.right):
            prevLevel += 1
            rightLevel, rightMinNode = self.__lowestCommonAncestor(node.right, p, q, prevLevel)
        if leftLevel == -1 and rightLevel == -1:
            return (prevLevel, node)
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

def main():
    tn = TreeNode(3, TreeNode(5, TreeNode(2, None, None), TreeNode(4, None, None)), TreeNode(1, TreeNode(6, None, None),
    TreeNode(7, None, None)))
    sol = Solution()
    print(sol.lowestCommonAncestor(tn, 5, 1))

if __name__ == "__main__":
    main()
