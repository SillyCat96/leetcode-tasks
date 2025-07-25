"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""

from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        

        counter = Counter(arr)
        counts = list(counter.values())  # [2, 3, 1, 2]
        are_counts_unique = len(counts) == len(set(counts))
        return are_counts_unique




# Зона тестирования
solver = Solution()
print(solver.uniqueOccurrences([-5,-5,1,5,0,-7]))

