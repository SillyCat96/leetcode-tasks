class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zero_count = 0
        max_length = 0

        # Итерируем правым указателем (right) по всему массиву
        for right in range(len(nums)):
            # Если текущий элемент nums[right] равен 0, увеличиваем счетчик нулей
            if nums[right] == 0:
                zero_count += 1
            
            # Пока количество нулей в текущем окне (nums[left...right]) превышает k
            while zero_count > k:
                # Если элемент, который покидает окно (nums[left]), равен 0,
                # уменьшаем счетчик нулей
                if nums[left] == 0:
                    zero_count -= 1
                # Сдвигаем левый указатель, чтобы сжать окно
                left += 1
            
            # Обновляем максимальную длину.
            # Длина текущего окна: right - left + 1
            max_length = max(max_length, right - left + 1)
            
        return max_length