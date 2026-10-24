class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #xor and then count the hamming number
        xor = start ^ goal
        count = 0
        while xor:
            xor &= (xor-1)
            count += 1
        return count
