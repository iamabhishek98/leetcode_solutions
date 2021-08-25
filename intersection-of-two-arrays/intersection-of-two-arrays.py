class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        
        common = set()
        i = 0
        j = 0
        
        while i < len(s1) and j < len(s2):
            curr_i = s1[i]
            curr_j = s2[j]

            if curr_i == curr_j:
                common.add(curr_i)
                i += 1
                j += 1
            elif curr_i < curr_j:
                i += 1
            else:
                j += 1
        
        return common
        
        
        
        