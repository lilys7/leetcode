class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        integer = 0
        #hashmap mapping every char to int value
        symbols = {'I': 1, 'V' : 5, 'X' : 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i+1 < len(s) and symbols[s[i]] < symbols[s[i+1]]:
                integer -= symbols[s[i]]
            else:
                integer += symbols[s[i]]

        return integer


        
