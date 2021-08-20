class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        min_pq = []
        for i in points:
            eucli_dis = math.sqrt(pow(i[0], 2) + pow(i[1], 2))    
            heapq.heappush(min_pq, [eucli_dis, i])
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(min_pq)[1])
        
        return ans