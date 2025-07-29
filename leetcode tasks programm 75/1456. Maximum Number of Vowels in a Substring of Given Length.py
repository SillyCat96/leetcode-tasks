"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
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
        cur_num = max_num = self.countVowels(s[:k])

        for r in range(k, len(s)):
            if s[r-k] in "aeiouAEIOU":
                cur_num -= 1
            if s[r] in "aeiouAEIOU":
                 cur_num += 1
            max_num = max(max_num, cur_num)
        return(max_num)
        

solver = Solution()
result = solver.maxVowels("abciiidef", 3)