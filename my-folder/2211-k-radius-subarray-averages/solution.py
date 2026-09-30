class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        res = [-1] * len(nums)
        window_size = 2 * k + 1
        if len(nums) < window_size:
            return res
        
        window_sum = sum(nums[:window_size])
        res[k] = window_sum // window_size

        for i in range(window_size, len(nums)):
            window_sum += nums[i] - nums[i - window_size]
            res[i-k] = window_sum // window_size
        return res



