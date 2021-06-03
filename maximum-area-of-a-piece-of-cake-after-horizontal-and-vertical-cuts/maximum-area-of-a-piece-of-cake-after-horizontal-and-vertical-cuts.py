class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        hcuts = [0]
        hcuts.extend(sorted(horizontalCuts))
        hcuts.append(h)
        vcuts = [0]
        vcuts.extend(sorted(verticalCuts))
        vcuts.append(w)
        
        maxh = max([(hcuts[i]-hcuts[i-1]) for i in range(1,len(hcuts))])
        maxw = max([(vcuts[i]-vcuts[i-1]) for i in range(1,len(vcuts))])
        
        return (maxh*maxw)%(1000000000+7)