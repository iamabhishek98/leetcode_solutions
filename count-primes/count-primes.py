class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0

        # sieve of eratosthenes
        # assume all numbers are prime
        nums = [True]*(n)
        nums[0] = nums[1] = False
        
        for i in range(2,int(sqrt(n)+1)):
            if nums[i]:
                mul = i*i
                while mul < n:
                    nums[mul] = False
                    mul += i
        
        return sum(nums)