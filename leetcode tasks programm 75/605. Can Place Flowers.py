class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        can_plant_flowers = None

        for pot in range(len(flowerbed)):
            if flowerbed[pot] == 0:
                left = 0 if pot == 0 else flowerbed[pot - 1]
                right = 0 if pot == len(flowerbed) - 1 else flowerbed[pot + 1]

                if left == 0 and right == 0:
                    flowerbed[pot] = 1
                    n -= 1
        can_plant_flowers = True if n <= 0 else False
        return can_plant_flowers   

## Зона тестирования 

# Создаем экземпляр класса Solution
solver = Solution()

print(f"Пример 1 ([1,0,0,0,1], 1): {solver.canPlaceFlowers([1,0,0,0,1], 1)}")
