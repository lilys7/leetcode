class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lp = 0
        rp = 1
        maxProfit = 0
        while rp < len(prices):
            if (prices[lp] < prices[rp]):
                maxProfit = max(maxProfit, prices[rp] - prices[lp])
            else:
                lp = rp
            rp += 1
        return maxProfit

            




        
