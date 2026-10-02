class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        lp = 0
        num = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[lp])
                lp += 1

            visited.add(s[r])
            num = max(num, len(visited))
        return num

            
            


