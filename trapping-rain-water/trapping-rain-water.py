class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = []
        m = 0
        for i in range(len(height)):
            m = max(m, height[i])
            left_max.append(m)
        
        right_max = []
        m = 0
        for i in range(len(height)-1,-1,-1):
            m = max(m, height[i])
            right_max.append(m)
        
        count = 0
        for i in range(len(height)):
            count += (min(left_max[i], right_max[len(height)-i-1]) - height[i])
        
        return count