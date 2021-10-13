class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # divide all weights into 2 groups
        # the minimum difference between the sum of these 2 groups is the answer
        
        # use dp to record the achievable diff of one group.
        # If x in the set dp, it means the difference x is achievable currently
        
        dp = set()
        # initial value of 0 because they are no stones
        dp.add(0)
        
        for stone in stones:
            new_dp = set()
            for x in dp:
                # the difference > initial value
                new_dp.add(stone+x)
                # the difference < initial value
                new_dp.add(abs(stone-x))
            dp = new_dp
            
        return min(dp)