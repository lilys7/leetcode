class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastPrev = 1
        for current in range(len(nums) - 1):
            if nums[current+1] > nums[current]: 
                nums[lastPrev] = nums[current+1]
                lastPrev = lastPrev + 1

        return lastPrev




        
