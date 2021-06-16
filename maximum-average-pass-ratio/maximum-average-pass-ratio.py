class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        change_in_pass_ratio = lambda currPass,currTotal: currPass/float(currTotal)-(currPass+1)/float(currTotal+1)
        max_pq = []
        
        for i in classes:
            heapq.heappush(max_pq, (change_in_pass_ratio(i[0],i[1]), i[0], i[1]))
        
        for _ in range(extraStudents):
            currPassRatio, currPass, currTotal = heapq.heappop(max_pq)
            heapq.heappush(max_pq, (change_in_pass_ratio(currPass+1,currTotal+1), currPass+1, currTotal+1))

        totalAvg = 0
        for _,p,t in max_pq:
            totalAvg += p/float(t)
            
        return totalAvg/float(len(classes))