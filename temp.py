
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the head of the new merged list.
        dummy_head = ListNode()
        current = dummy_head

        # Loop until one of the lists is exhausted.
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next

        # Attach the remaining nodes from the non-empty list.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts at the next node of the dummy head.
        return dummy_head.next