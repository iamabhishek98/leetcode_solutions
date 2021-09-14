class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum = 0
        sum_count = {}
        result = 0

        # because we have seen a sum of 0 once
        sum_count[0] = 1

        
        for i in nums:
            curr_sum += i

            # if curr_sum - k exists in the hashmap, it means we have seen a subarray which sums to k before
            if (curr_sum - k) in sum_count: 
                result += sum_count[curr_sum - k]
            
            sum_count[curr_sum] = sum_count.get(curr_sum, 0) + 1
        
        
        return result