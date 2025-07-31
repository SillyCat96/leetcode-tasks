class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        max_altitude = 0

        for change in gain:
            current_altitude += change

            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
    
solver = Solution()
print(solver.largestAltitude([-5,1,5,0,-7]))