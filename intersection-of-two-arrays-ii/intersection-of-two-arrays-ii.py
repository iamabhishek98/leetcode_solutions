from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        intersection = []
        
        for k1 in c1:
            intersection.extend(min(c1[k1],c2.get(k1,0))*[k1])
        
        return intersection