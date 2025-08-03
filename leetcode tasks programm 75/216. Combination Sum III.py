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
        
        def backtrack(k, n, start, current_combination):
            # 1. Базовый случай для успешной комбинации
            if n == 0 and k == 0:
                result.append(list(current_combination))
                return
            
            # 2. Условия для обрезки веток (оптимизация)
            if n < 0 or k < 0:
                return

            # 3. Рекурсивный шаг
            for i in range(start, 10):
                # Добавляем число в текущую комбинацию
                current_combination.append(i)
                
                # Рекурсивный вызов
                # Уменьшаем k на 1, n на i, начинаем поиск со следующего числа (i + 1)
                backtrack(k - 1, n - i, i + 1, current_combination)
                
                # Откат: удаляем последнее добавленное число, чтобы попробовать другие варианты
                current_combination.pop()


        backtrack(k, n, 1, []) #k = 3 n = 9
        
        return result
        


solver = Solution()
print(solver.combinationSum3(3,9))