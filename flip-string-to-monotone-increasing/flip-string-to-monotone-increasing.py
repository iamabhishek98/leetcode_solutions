class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://www.youtube.com/watch?v=Do2BcLMfyoE&ab_channel=CodingDecoded
        
        witnessOne = False
        zeroToOneCount = 0
        oneCount = 0
        
        for i in s:
            if i == "1":
                witnessOne = True
            if witnessOne:
                if i == "0": zeroToOneCount += 1
                else: oneCount += 1
                    
                zeroToOneCount = min(zeroToOneCount, oneCount)
        
        return min(zeroToOneCount, oneCount)