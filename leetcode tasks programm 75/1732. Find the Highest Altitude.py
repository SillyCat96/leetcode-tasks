"""
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.
"""
from collections import deque

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        array_gain = deque(gain)
        curr_sum = maxsum = 0
        while array_gain:
            curr_sum += array_gain[0]
            array_gain.popleft()
            maxsum = max(maxsum, curr_sum)

        return maxsum

# Зона тестирования
solver = Solution()
print(solver.largestAltitude([-5,1,5,0,-7]))

