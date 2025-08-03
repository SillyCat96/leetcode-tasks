"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

"""    
class Solution(object):
    def combinationSum2(self, candidates, target):
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
            
            # Рекурсивный шаг
            for i in range(start, len(candidates)):
                # Важное условие для предотвращения дубликатов.
                # Если текущее число такое же, как и предыдущее (i-1),
                # мы его пропускаем. Это работает, потому что массив отсортирован,
                # и мы гарантируем, что каждая уникальная ветка начинается
                # только с одного из этих одинаковых чисел.
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                current_combo.append(candidates[i])
                
                backtrack(target - candidates[i], i + 1, current_combo)
                
                current_combo.pop()

        backtrack(target, 0, [])
        
        return result

# Пример использования
solver = Solution()
print(solver.combinationSum2([10,1,2,7,6,1,5], 8)) 
        