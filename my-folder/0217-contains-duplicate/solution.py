class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # hashmap of all the values in nums, if the next element alr in the prevMap set, return true. else if all elements have been visited and we have not returned, ret false.
        prevMap = set()
        for num in nums:
            if num not in prevMap:
                prevMap.add(num)
            else:
                return True
        return False

        
