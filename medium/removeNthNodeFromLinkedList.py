# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr,  length = head, 0
        while curr is not None:
            length += 1
            curr = curr.next
        i, indexToRemove, curr, prev = 0, length - n, head, None
        while curr is not None:
            if i == indexToRemove:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            i += 1
        return head
                
    def printList(self, head: Optional[ListNode]):
        curr, s = head, ""
        while curr is not None:
            s += str(curr.val)
            curr = curr.next
        print(s)
