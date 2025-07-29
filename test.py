"""
Given a string s and an integer k, 
return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.




"""
class Solution(object):
    def countVowels(self, s):
        vowels = "aeiouAEIOU"
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiouAEIOU"
        max_substring = cur_substring = self.countVowels(s[:k])
        for r in range(k, len(s)):
            if s[r - k] in vowels:
                cur_substring -= 1
            if s[r] in vowels:
                cur_substring += 1
            max_substring = max(max_substring, cur_substring)
        return max_substring
        

# Зона тестирования
solver = Solution()
print(solver.maxVowels("abciiidef",3))


