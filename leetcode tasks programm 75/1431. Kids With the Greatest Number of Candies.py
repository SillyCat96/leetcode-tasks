class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        Входные данные: candies = [2,3,5,1,3], extraCandies = 3
        Выходные данные: [true,true,true,false,true]
        """
        can_have_most_candies = [] 
        max_candies = max(candies) 

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                can_have_most_candies.append(True) 
            else:
                can_have_most_candies.append(False) 

        return can_have_most_candies 


## Зона тестирования 

# Создаем экземпляр класса Solution
solver = Solution()

# Вызываем метод kidsWithCandies, используя экземпляр solver
# Оператор print() выведет результат, возвращенный функцией.
print(f"Пример 1 ([2,3,5,1,3], 3): {solver.kidsWithCandies([2,3,5,1,3], 3)}")
