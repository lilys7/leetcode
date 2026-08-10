class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hashmap with key index pair
        numMap = {}
        ret = []
        #enumerate index comes first
        for i, num in enumerate(nums):
            numMap[num] = i
        
        for n in range(len(nums)):
            sub = target - nums[n]
            if ((sub in numMap) and (n != numMap[sub])):
                ret.append(n)
                ret.append(numMap[sub])
                return ret
        return None
        
