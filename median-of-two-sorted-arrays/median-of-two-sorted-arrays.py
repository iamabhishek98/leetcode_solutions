class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """        
        # https://www.youtube.com/watch?v=lLFDQCDzfpI&ab_channel=CodingwithConner
        n = len(nums1)+len(nums2)
        
        def getMax(arr, partition):
            if partition == 0: return -sys.maxint+1
            return arr[partition-1]
    
        def getMin(arr, partition):
            if partition == len(arr): return sys.maxint
            return arr[partition]
        
        # scan through the smallest array to save us time        
        smaller = nums1
        larger = nums2
        
        if len(nums1)>len(nums2):
            smaller = nums2
            larger = nums1
        
        left = 0
        right = len(smaller)
        
        while left <= right:
            partX = (left+right)/2
            partY = (n+1)/2 - partX
            
            leftX = getMax(smaller, partX)            
            rightX = getMin(smaller, partX)
            
            leftY = getMax(larger, partY)            
            rightY = getMin(larger, partY)
            
            if leftX <= rightY and leftY <= rightX:
                if n%2==0:
                    return (max(leftX,leftY)+min(rightX,rightY))/2.0
                return max(leftX,leftY)
            
            elif leftX > rightY:
                right = partX-1
            else:
                left = partX+1