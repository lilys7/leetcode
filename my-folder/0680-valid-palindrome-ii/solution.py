class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #two pointers still, this time if we meet a difference the first time we can skip over and keep looking, but if afterwards still no lineup return false
        l = 0
        r = len(s) - 1
        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        while l < r:
            if s[l] != s[r]:
                return palindrome(l+1, r) or palindrome(l, r-1)
            l += 1
            r -= 1
        return True



        
