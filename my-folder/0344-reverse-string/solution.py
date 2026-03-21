class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #use two pointers and keep swapping
        f, l = 0, len(s) - 1
        while f < l:
            first = s[f]
            s[f] = s[l]
            s[l] = first
            f+=1
            l-=1
        

        
