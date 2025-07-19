
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """


        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

       
        if str1 + str2 != str2 + str1:
            return "" 

        len1 = len(str1)
        len2 = len(str2)
        
        
        gcd_length = find_gcd(len1, len2)

        result_string = str1[:gcd_length]

        return result_string

# --- Testing Zone ---
solver = Solution()

print(f"Example 1 (ABCABC, ABC): {solver.gcdOfStrings('ABCABC', 'ABC')}")
# Ожидаемый вывод: ABC

print(f"Example 2 (AAAA, ABC): {solver.gcdOfStrings('AAAA', 'ABC')}")
# Ожидаемый вывод: ""

print(f"Example 3 (LEET, CODE): {solver.gcdOfStrings('LEET', 'CODE')}")
# Ожидаемый вывод: ""

print(f"Custom Test (ACCCC, AC): {solver.gcdOfStrings('ACCCC', 'AC')}")
# Ожидаемый вывод: "" (т.к. ACCCC не состоит из повторений AC)

print(f"Custom Test (AAAAAA, AA): {solver.gcdOfStrings('AAAAAA', 'AA')}")
# Ожидаемый вывод: AA

print(f"Custom Test (ABCABCABC, ABCABC): {solver.gcdOfStrings('ABCABCABC', 'ABCABC')}")
# Ожидаемый вывод: ABC