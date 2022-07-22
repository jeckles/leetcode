# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)
        curr = res
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val, None)
                list1 = list1.next
            elif list2.val < list1.val:
                curr.next = ListNode(list2.val, None)
                list2 = list2.next
            curr = curr.next
        if list2 is not None:
            curr.next = list2
        elif list1 is not None:
            curr.next = list1
        return res.next
