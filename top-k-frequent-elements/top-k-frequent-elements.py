from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        
        max_pq = []
        for key in c:
            heapq.heappush(max_pq, tuple([-c[key],key]))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(max_pq)[1])
            
        return ans
        