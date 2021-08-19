class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        count = 0
        while i < m + count or j < n:
            if i < m + count and j < n:
                if nums1[i] > nums2[j]:
                    nums1.insert(i,nums2[j])
                    nums1.pop()
                    count += 1
                    i += 1
                    j += 1
                else:
                    i += 1
            elif j < n:
                nums1[i] = (nums2[j])
                i += 1
                j += 1     
            else:
                i += 1