class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sorting with two pointer approach
        
        nums.sort()
        closest_sum = 0
        abs_min = sys.maxint
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == target: return target
                
                diff = abs(target - curr_sum)
                if (diff < abs_min):
                    abs_min = diff 
                    closest_sum = curr_sum
                    
                if curr_sum < target: left += 1
                else: right -= 1
        
        return closest_sum
                