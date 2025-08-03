"""
    You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
    where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

    Input: head = [1,3,4,7,1,2,6]
    Output: [1,3,4,1,2,6]
    Explanation:
    The above figure represents the given linked list. The indices of the nodes are written below.
    Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
    We return the new list after removing this node. 

    Input: head = [1,2,3,4]
    Output: [1,2,4]
    Explanation:
    The above figure represents the given linked list.
    For n = 4, node 2 with value 3 is the middle node, which is marked in red.

    Input: head = [2,1]
    Output: [2]
    Explanation:
    The above figure represents the given linked list.
    For n = 2, node 1 with value 1 is the middle node, which is marked in red.
    Node 0 with value 2 is the only node remaining after removing node 1.
"""    
# Definition for a singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

class Solution(object):
        def deleteMiddle(self, head):
            """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            if not head or not head.next:
                return None

            # Создаем указатели
            slow = head
            fast = head
            prev = None  # prev будет хранить указатель на узел перед slow

            while fast and fast.next:
                prev = slow
                slow = slow.next
                
                fast = fast.next.next

            # После цикла slow указывает на средний узел, а prev — на узел перед ним
            # Удаляем средний узел, "перепрыгивая" через него
            prev.next = slow.next

            return head