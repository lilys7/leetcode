class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        count = [0] * 26
        #increment ord
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        for ch in t:
            count[ord(ch)-ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
        
