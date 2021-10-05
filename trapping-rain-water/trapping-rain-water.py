class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = []
        mx = height[0]
        for i in height:
            mx = max(mx,i)
            left_max.append(mx)
        
        right_max = []
        mx = height[-1]
        for i in range(len(height)-1,-1,-1):
            mx = max(mx,height[i])
            right_max.append(mx)
        right_max.reverse()

        trapped = 0
        for i,x in enumerate(height):
            trapped += (min(left_max[i],right_max[i])-x)
                
        return trapped