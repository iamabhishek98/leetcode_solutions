class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        
        # since we want the max we iterate from the back
        i = 0
        while i < len(citations) and citations[-1-i] > i:
            i += 1
        
        return i