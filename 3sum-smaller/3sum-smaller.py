class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        count = 0
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                curr_sum = nums[i]+nums[left]+nums[right] 
                if curr_sum < target:
                    # we do right-left because when the left element is paired 
                    # with any of the elements between left and right
                    # it is guaranteed to be less than or equal to the sum of the left and right pointer elements
                    # because the array is sorted
                    count += (right-left)
                    left += 1
                else:
                    right -= 1
        
        return count