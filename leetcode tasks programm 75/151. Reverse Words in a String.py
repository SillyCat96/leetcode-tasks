"""
Input: s = "the sky is blue"
Output: "blue is sky the"
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        word = ''

        words = s.split()   # встроенная функция

        '''
        функция написанная в ручную
        for ch in s:
            if not ch.isspace():
                word += ch
            elif word:
                words.append(word)
                word = ''
        if word:
            words.append(word)
        ''' 
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]

            left+=1
            right-=1

        return ' '.join(words)

## Зона тестирования 

# Создаем экземпляр класса Solution
solver = Solution()

print(f"Пример 1 (the sky is blue): {solver.reverseWords("the sky is blue")}")
