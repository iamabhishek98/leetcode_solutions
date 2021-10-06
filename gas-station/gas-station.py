class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        
        total_tank = 0
        curr_tank = 0
        starting_station = 0
        
        for i in range(n):
            total_tank += gas[i]-cost[i]
            curr_tank += gas[i]-cost[i]
            # if the current tank is negative means, one cannot get to the next stop 
            # so the current station cannot be the starting point 
            if curr_tank < 0:
                starting_station = i+1
                curr_tank = 0
        
        # if total tank is negative means the total cost > total gas available so making the trip is impossible
        return -1 if total_tank < 0 else starting_station