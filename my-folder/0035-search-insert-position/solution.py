class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            lastVal = nums[len(nums) - 1]
            if target > lastVal:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if(nums[i] > target):
                        return i
        else:
            return nums.index(target)

        

        
