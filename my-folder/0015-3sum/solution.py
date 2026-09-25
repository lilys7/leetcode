class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #basically two sum but extra loop O(n^2)?
        nums.sort()
        res = []
        for n in range(len(nums) - 2):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            lo = n+1
            hi = len(nums) - 1
            
            while lo < hi:
                total = nums[n] + nums[lo] + nums[hi]
                if total == 0:
                    res.append([nums[n],nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while nums[lo] == nums[lo-1] and lo < hi:
                        lo+=1
                    while nums[hi] == nums[hi+1] and lo < hi:
                        hi-=1

                #too low, move lo up
                elif total < 0:
                    lo += 1
                    
                else:
                    hi-=1
        return res

                
            
                
