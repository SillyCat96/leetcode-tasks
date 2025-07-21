"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0 
        right = len(height) - 1
        area = 0
        Max_area = 0
        while left < right:
            # Вычисляем текущую площадь, это правильно
            area = min(height[left], height[right]) * (right - left)
            
            if area > Max_area: # Или просто Max_area = max(Max_area, area)
                Max_area = area

            if height[left] < height[right]:
                left += 1  # Двигаем левый указатель вправо
            # Иначе (если высота правой линии меньше или равна высоте левой)
            else:
                right -= 1 # Двигаем правый указатель влево

        return Max_area


# Зона тестирования
solver = Solution()
print(solver.maxArea([1,8,6,2,5,4,8,3,7]))

