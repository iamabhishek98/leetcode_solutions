class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # https://www.youtube.com/watch?v=G5wLN4UweAM&ab_channel=alGOds
        n = len(matrix[0])
        
        start = matrix[0][0]
        end = matrix[-1][-1]
        
        while start<end:
            mid = start+(end-start)//2
            currPos = sum([bisect.bisect_right(row, mid) for row in matrix])
            
            if currPos<k: start = mid + 1
            else: end = mid
                
        return start