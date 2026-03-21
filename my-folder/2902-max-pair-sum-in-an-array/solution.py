class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find highest digit in each number and store in a hashmap with the highest
        #digit as the key and the num as the value
        groups = {} #max digit : value
        for i in nums:
            maximum = max(str(i))
            if maximum not in groups:
                groups[maximum] = []
            groups[maximum].append(i)
                
        max_sum = -1
        for vals in groups.values():
            if len(vals) >= 2:
                vals.sort(reverse=True)
                max_sum = max(max_sum, vals[0] + vals[1])
        return max_sum

