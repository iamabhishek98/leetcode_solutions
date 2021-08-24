class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        # use a set and count the len of set = right - left + 1 because the interval is inclusive
        # add to set only if between left and right
        
        occurrences = set()
        
        for rang in ranges:
            for i in range(rang[0],rang[1]+1):
                if left <= i <= right:
                    occurrences.add(i)
        
        return len(occurrences) == (right - left + 1)