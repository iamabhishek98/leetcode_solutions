class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if (len(str1)>=len(str2)):
            small = str2
            big = str1
        else:
            small = str1
            big = str2
        div = ""
        for i in range(len(small)):
            for j in range(i + 1, len(small) + 1):
                curr = (small[i:j])
                if (curr in big and len(big)%len(curr)==0 and len(small)%len(curr)==0 and len(curr)>len(div) 
                    and curr*(len(small)/len(curr))==small and curr*(len(big)/len(curr))==big):
                    div = curr
        return div
                    
                    
