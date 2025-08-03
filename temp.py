"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. 
The list must not contain the same combination twice, and the combinations may be returned in any order.

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations
"""    
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(k, n, start, current_combo):
            if k == 0 and n == 0:
                result.append(list(current_combo))
                return
            
            if k < 0 or n < 0:
                return
            
            for i in range(start, 10):
                current_combo.append(i)
                backtrack(k - 1, n - i, i + 1, current_combo)
                current_combo.pop()


        backtrack(k, n, 1, [])

        return result
        


solver = Solution()
print(solver.combinationSum3(3,9))