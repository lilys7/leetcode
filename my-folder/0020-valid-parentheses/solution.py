class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #use a stack and hashmap
        closing = { '}' : '{', ')' : '(', ']' : '['}
        seen = []
        for ch in s:
            if ch not in closing:
                seen.append(ch)
            else:
                if seen:
                    if ch in closing and closing[ch] != seen.pop():
                        return False
                else:
                    return False
        if not seen:
            return True
        else:
            return False



        
