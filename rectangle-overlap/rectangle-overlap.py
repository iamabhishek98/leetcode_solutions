class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2 = 0,1,2,3
        
        return (min(rec1[y2], rec2[y2]) - max(rec1[y1], rec2[y1]) > 0) and (min(rec1[x2], rec2[x2]) - max(rec1[x1], rec2[x1]) > 0)