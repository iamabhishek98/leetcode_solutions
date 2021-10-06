class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Let i and j be two pointers which splits the array into 3 parts. 
    
        # Condition for splitting: nums[i] <= nums[j]-nums[i] <= nums.back() - nums[j];
        
        # which can be simplified to -
        # 1. nums[j] >= 2*nums[i]                     --> (condition for left boundary of j)  
        # 2. nums[j] <= (nums.back() + nums[i]) / 2   --> (condition for right boundary of j)
        
        
        # contains the curr sum at each given element
        mod, pre_sum = int(1e9+7), [nums[0]]
        for num in nums[1:]:                               # create prefix sum array
            pre_sum.append(pre_sum[-1] + num)
        ans, n = 0, len(nums)
        for i in range(n):                                 # pre_sum[i] is the sum of the 1st segment
            prev = pre_sum[i]                              # i+1 is the starting index of the 2nd segment
            if prev * 3 > pre_sum[-1]: break               # break loop if first segment is larger than the sum of 2 & 3 segments
                
            j = bisect.bisect_left(pre_sum, prev * 2, i+1) # j is the first possible ending index of 2nd segment
                
            middle = (prev + pre_sum[-1]) // 2             # last possible ending value of 2nd segment
            k = bisect.bisect_right(pre_sum, middle, j+1)  # k-1 is the last possible ending index of 2nd segment
            if k-1 >= n or pre_sum[k-1] > middle: continue # make sure the value satisfy the condition since we are using bisect_right here
            ans = (ans + min(k, n - 1) - j) % mod          # count & handle edge case
        return ans