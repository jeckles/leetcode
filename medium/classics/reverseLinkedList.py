class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():

    def __init__(self, node):
        self.head = node
    
    def insert(self, val):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    def toString(self):
        string = ""
        curr = self.head
        while curr is not None:
            string += str(curr.val)
            curr = curr.next
        return string
    
    def reverse(self):
        prev = self.head
        curr = self.head.next
        prev.next = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev


def main():
    ll = LinkedList(Node(1))
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    print(ll.toString())
    ll.reverse()
    print(ll.toString())

if __name__ == "__main__":
    main()
