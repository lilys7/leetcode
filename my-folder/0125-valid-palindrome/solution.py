class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #use two pointers
        #strip the string
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            while lp < rp and not s[lp].isalnum():
                lp += 1
            while lp < rp and not s[rp].isalnum():
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True


        
