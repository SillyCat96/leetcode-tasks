"""
Файл для тестирования разных вещей

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

"""
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # 1. Инициализируем массивы для произведений слева и справа
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n

        # 2. Заполняем left_products
        # left_products[0] всегда 1 (нет элементов слева)
        # left_products[i] = nums[i-1] * left_products[i-1]
        for i in range(1, n):
            left_products[i] = nums[i - 1] * left_products[i - 1]

        # 3. Заполняем right_products
        # right_products[n-1] всегда 1 (нет элементов справа)
        # right_products[i] = nums[i+1] * right_products[i+1]
        for i in range(n - 2, -1, -1): # Идем справа налево
            right_products[i] = nums[i + 1] * right_products[i + 1]

        # 4. Вычисляем окончательный ответ
        # answer[i] = left_products[i] * right_products[i]
        for i in range(n):
            answer[i] = left_products[i] * right_products[i]
            
        return answer

# Зона тестирования
solver = Solution()
print(f"Пример 1: {solver.productExceptSelf([1, 2, 3, 4])}") # Ожидаемый: [24, 12, 8, 6]
print(f"Пример 2: {solver.productExceptSelf([-1, 1, 0, -3, 3])}") # Ожидаемый: [0, 0, 9, 0, 0]

            
            
            
