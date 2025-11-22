class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lastPrev = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[lastPrev] = nums[i]
                lastPrev+=1

        return lastPrev

        
