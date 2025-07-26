from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        
        # Шаг 1: Подсчитываем частоту каждой строки
        # Используем кортежи для строк, чтобы они были хешируемыми (могли использоваться в Counter)
        row_counts = Counter()
        for r in range(n):
            row_counts[tuple(grid[r])] += 1
        
        # Шаг 2: Извлекаем каждый столбец и проверяем его частоту среди строк
        equal_pairs_count = 0
        for c in range(n): # Итерируем по каждому индексу столбца
            current_col = []
            for r in range(n): # Собираем элементы текущего столбца
                current_col.append(grid[r][c])
            
            # Преобразуем столбец в кортеж, чтобы найти его в row_counts
            equal_pairs_count += row_counts[tuple(current_col)]
            
        return equal_pairs_count
    
# Пример 1
grid1 = [[3, 2, 1],
         [1, 7, 6],
         [2, 7, 7]]
solver1 = Solution()
result1 = solver1.equalPairs(grid1)
print(f"Для grid = {grid1}, количество равных пар: {result1}") # Ожидаем 1

