class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://www.youtube.com/watch?v=pmsex9gj1PI&ab_channel=CodingDecoded
        
        # sort the numbers for convenience
        nums.sort()
        
        ans = 0
        for i in range(2,len(nums)):
            left = 0
            right = i-1
            
            while left < right:
                # property of triangle is sum of any 2 sides should be greater than 1 side
                if nums[left]+nums[right]>nums[i]:
                    # right-left because left is the smallest side and if its sum with right is greater than the current side i, the sides which come after left (right of left) will also have a sum greater than the current side i
                    ans += (right-left)
                    # need to check if it is possible to reduce the maximum of the two pointers (right as right >= left) and see if the sum is still greater than the current side i
                    right -= 1
                # if the sum is not big enough, the left which is the minimum of the two pointers (left and right) should be the one to be increased, so the left pointer moves left
                else: left += 1
        
        return ans