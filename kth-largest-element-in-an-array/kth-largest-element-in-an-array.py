from sortedcontainers import SortedList, SortedSet, SortedDict 

class Solution(object):
    def findKthLargest(self, s, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_pq = []
        for i in s:
            heapq.heappush(max_pq,i)
        
        return heapq.nlargest(k,max_pq)[-1]