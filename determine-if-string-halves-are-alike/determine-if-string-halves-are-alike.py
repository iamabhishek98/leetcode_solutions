class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        c = 0
        mid = len(s)/2
        for i in range(mid):
            if s[i] in vowels:
                c += 1
            if s[mid+i] in vowels:
                c -= 1
        
        return c == 0
                    