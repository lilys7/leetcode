class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            curr = rp - lp // 2
            if nums[curr] == target:
                return curr
            elif nums[curr] > target:
                rp = curr - 1
            else:
                lp = curr + 1
        return -1

