# https://www.youtube.com/watch?v=c2LsK5-k7Lw

def generate(x):
    perm = []
    if x[0]=='0' and x[-1]=='0':
        if len(x) == 1:
            perm.append(x)
        return perm
    if x[0] == '0':
        perm.append("0."+x[1:])
        return perm
    if x[-1] == '0':
        perm.append(x)
        return perm
    perm.append(x)
    for i in range(1,len(x)):
        perm.append(x[0:i]+"."+x[i:])
    return perm

class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
            
        s = s[1:len(s)-1]
        for i in range(1,len(s)):
            llist = generate(s[0:i])
            rlist = generate(s[i:])
            for j in llist:
                for k in rlist:
                    ans.append("("+j+", "+k+")")
        return ans
                