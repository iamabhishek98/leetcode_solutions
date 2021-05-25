class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr)==1: return arr[0]
        n = len(arr)*0.25
        count = 1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]: count += 1
            else: count = 1
            if count>n: return arr[i]
        if count>n: return arr[-1]
        