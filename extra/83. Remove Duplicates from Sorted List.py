"""
Given the head of a sorted linked list, delete all duplicates 
such that each element appears only once. Return the linked list sorted as well..

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        dummy_head = ListNode()
        current = dummy_head
        seen_values = set()

        # Проходим по каждому узлу исходного списка
        while head is not None:
            if head.val not in seen_values:
                # 1. Привязываем текущий узел к новому списку
                # 2. Добавляем его значение в set
                # 3. Перемещаем наш "строительный" указатель
                current.next = head
                seen_values.add(head.val)
                current = current.next

            head = head.next

        # Последний узел в новом списке должен указывать на None
        current.next = None

        return dummy_head.next
        
