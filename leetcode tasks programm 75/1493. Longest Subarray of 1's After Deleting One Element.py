"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 
1's in the resulting array. Return 0 if there is no such subarray.

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = longest_streak = zeros = 0

        if 1 not in nums or len(nums) <= 1:
            return 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            longest_streak = max(longest_streak, right - left)

        return longest_streak

solver = Solution()
print(solver.longestSubarray([0,1,1,1,0,1,1,0,1]))