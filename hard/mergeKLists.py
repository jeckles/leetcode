from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''

 example case
 
 1 -> 4 -> 6 -> 8
 
 2 -> 9 -> 10
 
 6 -> 9 -> 12 -> 14

'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = resultPointer = ListNode(0, None)
        currMin, indexMin, curr, i = ListNode(float('inf'), None), 0, None, 0
        while i < len(lists) and len(lists) > 1:
            curr = lists[i]
            if curr.val < currMin.val:
                currMin = curr
                indexMin = i
            i += 1

            if i == len(lists): # made it to the end of the list
                resultPointer.val = currMin.val
                resultPointer.next = ListNode(0, None)
                resultPointer = resultPointer.next

                if currMin.next is None: # remove this index from lists
                    lists.pop(indexMin)
                else:
                    lists[indexMin] = lists[indexMin].next
                
                currMin = ListNode(float('inf'), None)
                i = 0

        if len(lists) > 0: # at this point there should be only one value left in the list
            resultPointer.val = lists[0].val
            resultPointer.next = lists[0].next
        
        self.toString(result)
        
        return result

    def toString(self, l):
        while l is not None:
            print(l.val)
            l = l.next
                    

def main():
    l1 = ListNode(1, ListNode(4, ListNode(6, ListNode(8, None))))
    l2 = ListNode(2, ListNode(9, ListNode(10, None))) 
    l3 = ListNode(6, ListNode(9, ListNode(12, ListNode(14, None)))) 

    sol = Solution()
    sol.mergeKLists([l1, l2, l3])

if __name__ == "__main__":
    main()
