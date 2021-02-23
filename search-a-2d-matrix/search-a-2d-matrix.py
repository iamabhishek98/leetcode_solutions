def binarySearch(row,x):
    i = 0
    j = len(row)
    while (i<=j):
        mid = i + (j-i)/2
        if (row[mid] == x):
            return True
        if (row[mid] > x):
            j = mid-1
        else:
            i = mid+1
    return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in matrix:
            if (target >= row[0] and target <= row[-1]):
                if binarySearch(row,target): return True
        return False