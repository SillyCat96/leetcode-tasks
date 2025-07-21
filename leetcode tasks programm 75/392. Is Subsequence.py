
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_pointer = 0
        
        if not s:
            return True
        
        for char_t in t: 
            if s_pointer < len(s) and s[s_pointer] == char_t:
                # Если совпало, двигаем указатель s_pointer на следующий символ
                s_pointer += 1
        
        return s_pointer == len(s)