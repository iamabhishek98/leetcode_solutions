class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        if n <= 2:
            return reversed(nums)
        
        prefix_product = [nums[0]]
        
        for i in range(1,n):
            prefix_product.append(prefix_product[-1]*nums[i])
        
        suffix_product = [nums[-1]]
        for i in range(n-2,-1,-1):
            suffix_product.append(suffix_product[-1]*nums[i])
        
        suffix_product.reverse()
        
        ans = []
        # the product of all other elements is essentially
        # (product of elements before curr element)*(product of elements after curr element)
        # first element has no before so we take all after
        # second element has no after so we take all before
        for i in range(n):
            if i == 0:
                ans.append(suffix_product[1])
            elif i == n-1:
                ans.append(prefix_product[-2])
            else:
                ans.append(prefix_product[i-1]*suffix_product[i+1])
        return ans