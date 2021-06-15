class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        perimeter = sum(matchsticks)
        possible_side = perimeter//4
        
        if possible_side*4 != perimeter: return False
        
        matchsticks.sort(reverse=True)
        lengths = [0 for _ in range(4)]        
        
        def dfs(i):
            if i == len(matchsticks):
                return lengths[0]==lengths[1]==lengths[2]==possible_side

            for side in range(4):
                if lengths[side] + matchsticks[i] <= possible_side:
                    lengths[side] += matchsticks[i]
                    
                    if dfs(i+1): return True
                    
                    lengths[side]-=matchsticks[i]
            
            return False
        
        return dfs(0)