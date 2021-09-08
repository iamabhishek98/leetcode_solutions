class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        total = sum(shifts)
        
        new_s = ""
        for i,x in enumerate(shifts):
            c = ord(s[i]) + (total % 26)
            if c > ord('z'):
                c -= 26
            new_s += (chr(c))
            total -= x
        
        return new_s
        