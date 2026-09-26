class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lp = 0
        rp = len(height) - 1
        maxArea = 0
        while lp < rp:
            area = min(height[lp], height[rp]) * (rp - lp)
            maxArea = max(maxArea, area)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return maxArea
        
