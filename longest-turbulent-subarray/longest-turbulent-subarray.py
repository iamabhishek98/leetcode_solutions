class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxLen = 0
        currLen = 0
        
        for i in range(len(arr)):
            if i>=2 and ((arr[i-2]<arr[i-1]>arr[i]) or (arr[i-2]>arr[i-1]<arr[i])):
                currLen+=1
            elif i>=1 and arr[i-1]!=arr[i]:
                currLen = 2
            else:
                currLen = 1
            maxLen = max(maxLen, currLen)
        
        return maxLen