class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3)!=(len(s1)+len(s2)): return False
        self.dp = {}
        def recurse(i,j,curr,st):
            key = str(i)+':'+str(j)+':'+str(curr)
            if key in self.dp: return self.dp[key]
            if (( i<len(s1) and s3[curr] != s1[i]) and ( j<len(s2) and s3[curr] != s2[j])): 
                return False
            if curr==len(s3): return True
    
            a = False
            b = False
            if i<len(s1) and s1[i] == s3[curr]:
                a =  recurse(i+1,j,curr+1,st+s1[i])
            if j<len(s2) and s2[j] == s3[curr]:
                b = recurse(i,j+1,curr+1,st+s2[j])
            self.dp[key] = a or b
            return self.dp[key]
        
        return recurse(0,0,0,"")