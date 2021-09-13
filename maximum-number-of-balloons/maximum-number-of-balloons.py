from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        m = Counter(text)
        
        return min(m.get('b',0), m.get('a',0), m.get('n',0), m.get('o',0)//2, m.get('l',0)//2)