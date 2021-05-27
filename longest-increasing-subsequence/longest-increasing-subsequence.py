class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for i in range(len(nums))]
        m = 1
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    m = max(m,dp[i])
        return m