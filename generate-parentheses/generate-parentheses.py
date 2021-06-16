class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def recurse(opening_count,closing_count,s):
            if len(s) == 2*n: 
                ans.append(s)
                return
            
            if opening_count < n:
                recurse(opening_count+1,closing_count,s+"(")
            
            if closing_count < opening_count:
                recurse(opening_count,closing_count+1,s+")")
                
        recurse(0,0,"")
        return ans