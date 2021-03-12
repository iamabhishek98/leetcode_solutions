class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i],1+dp[i-j])
        
        return -1 if dp[amount]>amount else dp[amount] 