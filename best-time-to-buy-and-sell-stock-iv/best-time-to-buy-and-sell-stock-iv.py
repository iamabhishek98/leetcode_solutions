class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        if n <= 0 or k <= 0: return 0
        
        # A transaction consists of two parts: buying and selling. 
        # Therefore, we need to find 2k points in the stock line, k points for buying, and k points for selling.
        # if 2k is larger than n, we are not able to pick 2k points from n points, 
        # which means we will not reach the limit no matter how we try. 
        # Therefore, all we need to do is to iterate each day, and if the price of day i arise, 
        # buy the stock in i-1th day and sell it at ith day.
        if (2*k>n):
            maxprofit = 0 
            for i in range(1,n):
                maxprofit += max(0,prices[i]-prices[i-1])
            return maxprofit
        
        # We can use dp[day_number][used_transaction_number][stock_holding_status] to represent our states, 
        # where stock_holding_status is a 0/1 number representing whether you hold the stock or not
        dp = [[[-sys.maxint+1 for _ in range(2)] for __ in range(k+1)] for ___ in range(len(prices))]
        
        # starting point is buying the stock on the first day
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        
        for i in range(1,n):
            for j in range(k+1):
                # hold stock
                dp[i][j][1] = max(dp[i][j][1],dp[i-1][j][1])
                
                # not hold stock
                dp[i][j][0] = max(dp[i][j][0],dp[i-1][j][0])
                
                if j > 0:
                    # buy stock
                    dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0] - prices[i])
                
                # sell stock
                dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][1] + prices[i])                
        
        # since there are at most j transactions, we need to see which no. of transactions gave max profit
        return max(dp[n-1][j][0] for j in range(k+1))