class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, head):
        self.head = head
        self.string = ""

    def insert(self, x):
        if x <= self.head.val:
            self.head.left = self.__insertHelper(self.head.left, x)
        else:
            self.head.right = self.__insertHelper(self.head.right, x)

    def __insertHelper(self, node, x):
        if node is None:
            return Node(x, None, None)
        else:
            if x <= node.val:
                node.left = self.__insertHelper(node.left, x)
            else:
                node.right = self.__insertHelper(node.right, x)
        return node

    def reverse(self):
        self.head = self.__reverseHelper(self.head)

    def __reverseHelper(self, node):
        if node.left is None and node.right is not None:
            left = node.left
            node.left = None
            node.right = left
            return node
        elif node.right is None and node.left is not None:
            right = node.right
            node.right = None
            node.left = right
            return node
        elif node.right is None and node.left is None:
            return node
        else:
            left = node.left
            node.left = self.__reverseHelper(node.right)
            node.right = self.__reverseHelper(left)
            return node

    def asString(self): # returns in order string traversal of BinaryTree...
        return self.__asStringHelper(self.head)

    def __asStringHelper(self, node):
        stringRep = ""
        if node is not None:
            stringRep += str(node.val)
            stringRep += self.__asStringHelper(node.left)
            stringRep += self.__asStringHelper(node.right)
        return stringRep

def main():
    bt = BinaryTree(Node(5, None, None))
    bt.insert(8)
    bt.insert(9)
    bt.insert(6)
    bt.insert(2)
    bt.insert(3)
    bt.insert(1)
    print("bt before reverse: " + bt.asString())
    bt.reverse()
    print("bt after reverse: " + bt.asString())

if __name__=="__main__":
    main()
