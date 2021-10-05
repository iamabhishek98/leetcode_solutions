class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = -1
        i2 = -1
        min_dist = sys.maxint
        
        for i,word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            if word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_dist = min(min_dist, abs(i1-i2))
        
        return min_dist