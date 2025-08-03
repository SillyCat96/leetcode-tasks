"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
"""

# Definition for a singly-linked list.
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

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ДЛЯ ТЕСТИРОВАНИЯ ---

# Функция для создания связанного списка из обычного списка Python
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Функция для вывода связанного списка в виде обычного списка Python
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)

# --- ТЕСТИРОВАНИЕ ---

solver = Solution()

# 1. Тест с примером [1,2,4] и [1,3,4]
list1_ll = create_linked_list([1, 2, 4])
list2_ll = create_linked_list([1, 3, 4])
merged_list = solver.mergeTwoLists(list1_ll, list2_ll)
print("Результат для [1,2,4] и [1,3,4]:")
print_linked_list(merged_list) 
# Ожидаемый вывод: [1, 1, 2, 3, 4, 4]

# 2. Тест с пустыми списками
list3_ll = create_linked_list([])
list4_ll = create_linked_list([])
merged_list = solver.mergeTwoLists(list3_ll, list4_ll)
print("\nРезультат для [] и []:")
print_linked_list(merged_list)
# Ожидаемый вывод: []

# 3. Тест с одним пустым списком
list5_ll = create_linked_list([])
list6_ll = create_linked_list([0])
merged_list = solver.mergeTwoLists(list5_ll, list6_ll)
print("\nРезультат для [] и [0]:")
print_linked_list(merged_list)
# Ожидаемый вывод: [0]

        