"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""
from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_counts = Counter(nums)
        operations = 0
        
        for num in list(num_counts.keys()):
            complement = k - num 
            
            if num_counts[num] > 0 and num_counts[complement] > 0:
                
                if num == complement:
                    ops_for_num = num_counts[num] // 2
                    operations += ops_for_num
                    num_counts[num] -= (ops_for_num * 2) 
                else:
                    ops_for_pair = min(num_counts[num], num_counts[complement])
                    operations += ops_for_pair
                    
                    num_counts[num] -= ops_for_pair
                    num_counts[complement] -= ops_for_pair
                    
        return operations


solver = Solution()
print(solver.maxOperations([1,2,3,4],5))