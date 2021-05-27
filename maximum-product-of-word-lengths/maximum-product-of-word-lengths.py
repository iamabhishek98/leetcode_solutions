class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitmask = defaultdict(int)
        for word in words:
            for i in word:
                bitmask[word] |= 1<<(ord(i) - 97)
        
        m = 0
        for i in words:
            for j in words:
                if bitmask[i]&bitmask[j]==0:
                    m = max(m,len(i)*len(j))       
        return m