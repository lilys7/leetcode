class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #need a stack to keep track, return true if the stack is empty once
        #everything removed, return false otherwise
        stack = []
        closeToOpenMap = {")": "(", "]":"[", "}":"{"}
        for c in s:
            #we wanna see if c is a cloing bracket
            if c in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        
