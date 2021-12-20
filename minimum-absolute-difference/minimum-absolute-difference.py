class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = sys.maxint
        
        for i in range(1,len(arr)):
            min_diff = min(min_diff,abs(arr[i]-arr[i-1]))
        
        l = []
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1]) == min_diff:
                l.append([arr[i-1],arr[i]])
        
        return l