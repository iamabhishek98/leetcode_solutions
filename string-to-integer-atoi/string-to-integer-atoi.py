class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign=1
        s=s.strip()
        if s=="": 
            return 0
        
        char=s[0]
        if char=="-" or char=="+":
            s=s[1:]
            if char=="-":
                sign=-1
        
        ans=0
        for ch in s:
            if '0'<=ch<='9':
                ans=ans*10+(int(ch))
            else:
                break
        
        ans *= sign
        maxint = 2**31
        if ans > (maxint-1): return (maxint-1)
        if ans < (-maxint): return (-maxint)
        return ans