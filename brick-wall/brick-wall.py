class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        freq = {}
        m = 0
        for row in wall:
            idx = 0
            for i in range(len(row)-1):
                idx += row[i]
                if idx in freq: freq[idx]+=1
                else: freq[idx]=1
                m = max(m,freq[idx])
        
        return len(wall)-m