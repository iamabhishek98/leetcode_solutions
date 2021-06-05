class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        # https://www.youtube.com/watch?v=aUkWh7hIzyY&list=PLEvw47Ps6OBCOkEO2QrbywrfEIZ0J30N3&index=3&ab_channel=CodeWithSunny
        
        candidates = zip(efficiency,speed)
        
        # sort candidates in descending order by their efficiency
        candidates  = sorted(candidates, key=lambda t:t[0], reverse=True)
        print candidates
        
        curr_team_speeds = []
        sum_speed = 0
        max_performance = 0
        
        for curr_efficiency, curr_speed in candidates:
            # if team has reached a size of k members
            if len(curr_team_speeds)>k-1:
                # remove team member with lowest speed
                sum_speed-=heapq.heappop(curr_team_speeds)
            
            # put current candidate to the team
            heapq.heappush(curr_team_speeds,curr_speed)
            sum_speed+=curr_speed
            
            # check if the performance is maximised with this member in the team 
            max_performance = max(max_performance, sum_speed*curr_efficiency)
        
        return max_performance % (10**9+7)
                