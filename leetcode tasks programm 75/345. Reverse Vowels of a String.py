class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')  # Для быстрого поиска гласных
        s_list = list(s)            # Преобразуем строку в список для мутабельности
        left, right = 0, len(s) - 1

        while left < right:
            # Двигаем left пока не гласная
            while left < right and s_list[left] not in vowels:
                left += 1
            # Двигаем right пока не гласная
            while left < right and s_list[right] not in vowels:
                right -= 1

            # Меняем гласные местами
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)
    
    
## Зона тестирования 

# Создаем экземпляр класса Solution
solver = Solution()

print(f"Пример 1 (LeetCode): {solver.reverseVowels("LeetCode")}")
