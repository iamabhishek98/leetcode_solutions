class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        # concept: https://www.youtube.com/watch?v=UiYVToWORMY&ab_channel=alGOds
        # code: https://www.youtube.com/watch?v=BeyJboRnKDI&ab_channel=CompetitiveCoder
        
        # idea: sum(d,f,target) = sum(d-1,f,target-1) + sum(d-1,f,target-2) + ... + sum(d-1,f,target-f)
        #       => sum(d,f,target) = summation(1 to f)(sum(d-1,f,target-i))
        
        dp = {}
        
        def recurse(d,f,target):
            key = str(d)+":"+str(target)
            if key in dp: return dp[key]
            
            # base cases
            # 1. if target is less than the number of dices, it is impossible to reach the target as min = d*1
            # 2. if target is greater than f*d, it is impossible also as max = f*d
            # 3. if 1 dice is left and target is greater than the f, it is impossible also
            if target < d or f*d < target: return 0
            if d == 1:
                if target <= f: return 1
                return 0
            
            s = 0
            for i in range(1,f+1):
                s += recurse(d-1,f,target-i)
            s %= (pow(10,9)+7)
            
            dp[key] = s
            return s
        
        return recurse(d,f,target)
        
        