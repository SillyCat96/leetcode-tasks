"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack = []
        str_stack = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Сохраняем текущую строку и множитель в стеки
                str_stack.append(current_str)
                num_stack.append(current_num)
                
                # Обнуляем переменные для нового вложенного уровня
                current_str = ""
                current_num = 0
            elif char == ']':
                # Извлекаем последний множитель и строку из стеков
                num = num_stack.pop()
                prev_str = str_stack.pop()
                
                # Выполняем повторение и объединяем строки
                current_str = prev_str + current_str * num
            else:
                # Если это буква, добавляем её к текущей строке
                current_str += char

        return current_str


solver = Solution()
print(solver.decodeString("3[a]2[bc]"))