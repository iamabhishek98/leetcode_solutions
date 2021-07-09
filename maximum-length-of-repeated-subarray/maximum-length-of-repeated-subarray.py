class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # https://www.youtube.com/watch?v=BgLVRkA8w6w&ab_channel=TimothyHChang
        dp = [[0 for _ in range(len(nums2)+1)] for __ in range(len(nums1)+1)]
        
        # top down dp approach
        # loop through the num1 and num2 array and add 1 to the prev diagonal, if the current cells are equal
        # get the maximum of all cells to know the length of the longest common subarray
        m = 0
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    m = max(m,dp[i][j])
        return m