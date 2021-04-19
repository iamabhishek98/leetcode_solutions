class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = []
        while n > 0:
            s.append(n%2)
            n/=2
            
        s = s[::-1]
        while len(s)<32:
            s.insert(0,0)
        
        ans = 0
        for i,x in enumerate(s):
            ans += x*pow(2,i)
        
        return ans