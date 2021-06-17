class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: int
        """
        # https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/1278426/JS-Python-Java-C%2B%2B-or-Easy-Triangular-Number-Solution-w-Explanation
        
        ans = 0
        lower_than_right = 0
        lower_than_left = 0
        for i in nums:
            if i > right: lower_than_right = 0
            if i >= left: lower_than_left = 0
            if i <= right:
                lower_than_right += 1
                ans += lower_than_right
            if i < left:
                lower_than_left += 1
                ans -= lower_than_left
        return ans
            