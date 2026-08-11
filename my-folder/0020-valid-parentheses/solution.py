class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #hashmap type pairs
        pairs = { ')' : '(', ']' : '[', '}' : '{'}
        chars = list(s)
        stack = []
        for ch in chars:
            if ch not in pairs:
                stack.append(ch)
            else:
                if stack and pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        return False
        


        
