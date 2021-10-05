class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {
            "D": [1,0],
            "R": [0,1],
            "U": [-1,0],
            "L": [0,-1],
         }
        
        i = 0
        j = 0
        
        for move in moves:
            i += d[move][0]            
            j += d[move][1]
        
        return i == 0 and j == 0

        