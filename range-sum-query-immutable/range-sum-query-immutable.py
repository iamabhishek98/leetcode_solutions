class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        curr_sum = 0
        for i in nums:
            curr_sum += i
            self.sums.append(curr_sum)
            
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0: return self.sums[right]
        return self.sums[right] - self.sums[left - 1] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)