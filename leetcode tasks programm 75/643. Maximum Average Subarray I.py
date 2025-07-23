class Solution(object):
    def findMaxAverage(self, nums, k): # Removed type hints: nums: list[int], k: int, -> float
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Шаг 1: Инициализация первого окна
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Шаг 2: Скольжение окна
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
            
        # Шаг 3: Вычисление среднего
        return float(max_sum) / k