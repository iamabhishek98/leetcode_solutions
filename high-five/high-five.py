import heapq

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        m = {}
        for item in items:
            if item[0] not in m: 
                m[item[0]] = [-item[1]]
                heapq.heapify(m[item[0]])
            else: 
                heapq.heappush(m[item[0]], -1*item[1])
        
        averages = []
        heapq.heapify(averages)
        for key in m:
            count = 0
            avg = 0
            while count < 5 and m[key]:
                avg += (-1*heapq.heappop(m[key]))
                count += 1
            avg /= count
            heapq.heappush(averages,[key,avg])
        
        ans = []
        while averages:
            ans.append(heapq.heappop(averages))
        
        return ans