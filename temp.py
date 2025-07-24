"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
"""
from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
       
        # Шаг 1: Проверяем длину
        if len(word1) != len(word2):
            return False

        # Шаг 2: Подсчитываем частоты символов
        count1 = Counter(word1)
        count2 = Counter(word2)
        # Шаг 3: Проверяем набор уникальных символов
        # Должны иметь одинаковые символы, независимо от их частоты
        # Используем set(count1.keys()) для получения уникальных символов
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Шаг 4: Проверяем набор частот (значений)
        # Сортируем списки частот и сравниваем их.
        # Например, если count1 = {'a': 2, 'b': 1} и count2 = {'c': 2, 'd': 1},
        # то list(count1.values()) = [2, 1] и list(count2.values()) = [2, 1].
        # После сортировки они будут [1, 2] и [1, 2], что совпадает.
        if sorted(count1.values()) != sorted(count2.values()):
               return False
        
        # Если все проверки пройдены, строки являются "близкими"
        return True






# Зона тестирования
solver = Solution()
print(solver.closeStrings("abc","bca"))

