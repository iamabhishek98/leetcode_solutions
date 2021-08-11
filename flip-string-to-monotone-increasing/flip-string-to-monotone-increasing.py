class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://www.youtube.com/watch?v=Do2BcLMfyoE&ab_channel=CodingDecoded
        
        # algo:
        # We loop through the string.
        # If we got a 1, go on. No need to flip. We just increment the 1 counter.
        # If we got a 0, we increment the flips counter.
        # Now, we have two options. Either to flip the new zero to one or to flip all previous ones to zeros.
        # So we take the min between flips and counter at every step of the way.
        
        witnessOne = False
        flipZeroToOneCount = 0
        oneCount = 0
        
        for i in s:
            if i == "0" and not witnessOne: continue
            witnessOne = True
            
            if i == "0": flipZeroToOneCount += 1
            else: oneCount += 1  
            
            flipZeroToOneCount = min(flipZeroToOneCount, oneCount)
        
        return flipZeroToOneCount