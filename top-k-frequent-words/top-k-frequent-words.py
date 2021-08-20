class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c = Counter(words)
        
        max_pq = []
        for key in c:
            heapq.heappush(max_pq, tuple([-c[key],key]))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(max_pq)[1])
            
        return ans
        