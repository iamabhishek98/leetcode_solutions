from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charMap = Counter(chars)
        totalSum = 0
        
        for word in words:
            currMap = Counter(word)
            status = True
            
            for c in currMap:
                if c not in charMap or currMap[c] > charMap[c]: status = False
            
            if status:
                totalSum += len(word)
        
        return totalSum