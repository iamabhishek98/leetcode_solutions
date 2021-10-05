class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://www.youtube.com/watch?v=qVfjmkL1naw&ab_channel=Pepcoding
        dp = [0]*(10**4+1)
        
        
        # creating a freq arr
        for i in nums:
            dp[i]+=1
        
        inc = 0
        exc = 0
        
        # at any given integer, the number of points we get is included = this number*freq + excluded at the prev number
        # excluded at current number = maximum of included and excluded at prev number
        
        # this way when we take the max of inc and exc as val for curr exc, we ignore the previous adjacent num (i-1)
        
        # and since we iterating over the array from 0...n, we always ignore the next adjacent num (i+1) 
        # so there's no need to account for that 
        for i in range(len(dp)):
            ni = dp[i]*i + exc
            ne = max(inc,exc)
            
            inc,exc = ni,ne
        
        return max(inc,exc)