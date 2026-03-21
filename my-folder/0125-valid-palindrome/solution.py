class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #strip the string and make all lowercase
        #if reversed v is the same, ret true
        f, l = 0, len(s) - 1
        s = s.lower()
        while f < l:
            if not(s[f].isalnum()):
                f+=1
                continue
            if not(s[l].isalnum()):
                l-=1
                continue
            if s[f] != s[l]:
                return False
            f+=1
            l-=1
        return True


        
