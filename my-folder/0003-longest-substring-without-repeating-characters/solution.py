class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lp = 0
        maxLen = 0
        seen = set()
        for rp in range(len(s)):
            while s[rp] in seen:
                seen.remove(s[lp])
                lp += 1
            seen.add(s[rp])
            maxLen = max(maxLen, rp - lp +1)
        return maxLen

