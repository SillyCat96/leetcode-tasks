from collections import Counter

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Шаг 1: Подсчитываем частоту каждого числа в nums
        # collections.Counter - это специализированный словарь для подсчета хешируемых объектов.
        num_counts = Counter(nums)
        operations = 0
        
        # Шаг 2: Итерируем по уникальным числам и их количествам в Counter
        # Используем list(num_counts.keys()) чтобы избежать ошибки "RuntimeError: dictionary changed size during iteration"
        # если мы будем изменять num_counts внутри цикла
        for num in list(num_counts.keys()):
            complement = k - num # Вычисляем "дополнение", которое необходимо для суммы k
            
            if num_counts[num] > 0 and num_counts[complement] > 0:
                
                if num == complement:
                    # Случай 1: Число равно своему дополнению (например, k=6, num=3, complement=3)
                    # Мы можем сформировать пары только из четного количества таких чисел.
                    # Например, если у нас 3 тройки, мы можем сделать только одну пару (3,3).
                    ops_for_num = num_counts[num] // 2
                    operations += ops_for_num
                    # Уменьшаем количество использованных чисел в Counter
                    num_counts[num] -= (ops_for_num * 2) 
                else:
                    # Случай 2: Число и его дополнение разные (например, k=5, num=1, complement=4)
                    # Количество пар, которые мы можем сформировать, ограничено наименьшим 
                    # количеством из этих двух чисел.
                    ops_for_pair = min(num_counts[num], num_counts[complement])
                    operations += ops_for_pair
                    
                    # Уменьшаем количество использованных чисел в Counter для обоих чисел
                    num_counts[num] -= ops_for_pair
                    num_counts[complement] -= ops_for_pair
                    
        return operations