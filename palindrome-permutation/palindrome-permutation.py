from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = Counter(s)
        
        odd = False
        for c in freq:
            v = freq[c]%2
            if v != 0:
                if odd: return False
                odd = True
        return True
            