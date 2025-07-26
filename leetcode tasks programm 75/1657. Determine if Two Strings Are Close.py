from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        counter_word1 = Counter(word1)
        counter_word2 = Counter(word2)

        if len(word1) != len(word2):
            return False
        
        if (counter_word1.keys()) != (counter_word2.keys()):
            return False

        if sorted(counter_word1.values()) != sorted(counter_word2.values()):
            return False
        
        return True 




solver = Solution()
print(solver.closeStrings("pen","nep"))