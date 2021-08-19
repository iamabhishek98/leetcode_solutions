class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # https://www.youtube.com/watch?v=zp4huR7LN6M&ab_channel=KeepOnCoding
        
        # move the pointers from right to left
        m -= 1
        n -= 1
        # the main pointer
        index = len(nums1) - 1
        
        while index >= 0:
            # if we reached end of first list
            if m < 0 and n >= 0:
                nums1[index] = nums2[n]
                n -= 1
            # if we reached end of second list
            elif n < 0 and m >= 0:
                nums1[index] = nums1[m]
                m -= 1
            # otherwise compare and add the one which is larger (because we are going from right to left)
            else:
                if nums1[m] < nums2[n]:
                    nums1[index] = nums2[n]
                    n -= 1
                else:
                    nums1[index] = nums1[m]
                    m -= 1
            index -= 1
