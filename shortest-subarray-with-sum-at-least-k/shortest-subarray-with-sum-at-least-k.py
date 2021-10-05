from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = []
        sums.append(0)
        
        # we want this sums array to be an non decreasing array
        for i in nums:
            sums.append(sums[-1]+i)
        
        q = deque()
        min_len = sys.maxint
        for i in range(len(nums)+1):
            while q and sums[i]-sums[q[0]] >= k:
                min_len = min(min_len,i-q[0])
                q.popleft()

            while q and sums[i] <= sums[q[-1]]:
                q.pop()
            
            q.append(i)
                    
        return -1 if min_len == sys.maxint else min_len