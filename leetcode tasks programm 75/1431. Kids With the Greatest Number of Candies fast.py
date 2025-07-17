class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        Входные данные: candies = [2,3,5,1,3], extraCandies = 3
        Выходные данные: [true,true,true,false,true]
        """
        
        max_candies = max(candies) 

        # Шаг 2: Используем генератор списка для создания нового списка булевых значений.
        # Для каждого ребенка (candy) в списке candies мы проверяем условие:
        # (candy + extraCandies >= max_candies)
        # Результат этого булевого выражения (True или False) добавляется в новый список.
        can_have_most_candies = [
            (candy + extraCandies >= max_candies) 
            for candy in candies
        ]
        
        return can_have_most_candies 

# Создаем экземпляр класса Solution
solver = Solution()

# Вызываем метод kidsWithCandies, используя экземпляр solver
print(f"Пример 1 ([2,3,5,1,3], 3): {solver.kidsWithCandies([2,3,5,1,3], 3)}") 
# Ожидаемый вывод: [True, True, True, False, True]
