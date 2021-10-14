from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        
        # method 1: min heap
        min_heap = []
        heapq.heapify(min_heap)
        for key in c:
            heapq.heappush(min_heap, [c[key],key])
            if len(min_heap) > k: heapq.heappop(min_heap)
        
        ans = []
        while min_heap:
            ans.append(heapq.heappop(min_heap)[1])
        return ans
        
#         # method 2: max heap        
#         max_heap = []
#         heapq.heapify(max_heap)

#         for key in c:
#             heapq.heappush(max_heap, tuple([-c[key],key]))
        
#         ans = []
#         for i in range(k):
#             ans.append(heapq.heappop(max_heap)[1])
            
#         return ans
        