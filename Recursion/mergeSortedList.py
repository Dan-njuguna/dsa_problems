# #!/usr/bin/python3
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        # list1: [1, 2, 4]
        # list2: [1, 3, 4]
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next


if __name__  == "__main__":
    # Test case 1
    list1 = ListNode(1, ListNode(2, ListNode(4)))  # 0 -> 1 -> 2 -> 4 -> null
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    while result:
        print(result.val)
        result = result.next

    # Test case 2
    list1 = ListNode(1)
    list2 = ListNode(2, ListNode(3, ListNode(4, ListNode(5))))
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    while result:
        print(result.val)
        result = result.next
