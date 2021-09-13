from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        m = Counter(text)
        
        if 'b' not in m: return 0
        count = m['b']
        
        if 'a' not in m: return 0
        count = min(count, m['a'])
        
        if 'n' not in m: return 0
        count = min(count, m['n'])
        
        if 'o' not in m or m['o'] < 2: return 0
        count = min(count, m['o']//2)
        
        if 'l' not in m or m['l'] < 2: return 0
        count = min(count, m['l']//2)
        
        return count