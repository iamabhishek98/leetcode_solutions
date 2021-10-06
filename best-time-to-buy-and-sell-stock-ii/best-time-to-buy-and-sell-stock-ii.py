class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find valley first and then find immediate next peak to maximise profit
        maxprofit = 0
        valley = prices[0]
        peak = prices[0]
        i = 0
        
        while i < len(prices):
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxprofit += (peak - valley)
            i += 1
        
        return maxprofit