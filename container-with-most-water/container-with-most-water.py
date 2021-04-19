class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        p1 = 0
        p2 = len(height)-1
        while p1<p2:
            m = max(m, min(height[p1],height[p2])*(p2-p1))
            if height[p1]<height[p2]: p1+=1
            else: p2-=1
        return m