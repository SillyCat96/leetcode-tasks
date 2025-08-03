"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique 
combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the giv

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []
"""    
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        candidates.sort()

        def backtrack(target, start, current_combo):
            if target == 0:
                result.append(list(current_combo))
                return
            
            if target < 0:
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
            
                current_combo.append(candidate)

                backtrack(target - candidate, i, current_combo)
                
                current_combo.pop()

        backtrack(target, 0, [])
        
        return result

# Пример использования
solver = Solution()
print(solver.combinationSum([2,3,6,7], 7)) # Ожидаемый вывод: [[2, 2, 3], [7]]
        