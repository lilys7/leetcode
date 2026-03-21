class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        char_str = collections.deque(s)
        for i in range(len(s)):
            joined = "".join(char_str)
            if (joined == goal):
                return True
            char_str.rotate(1)
        return False
        
