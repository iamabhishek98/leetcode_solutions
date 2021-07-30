class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        # store all the states in a map
        memo = {}
        states = []
        day = 0
        while day < n:
            day += 1
            
            # update the state
            states.append([0]*8)
            for i in range(1,7):
                if (cells[i-1] and cells[i+1]) or (not cells[i-1] and not cells[i+1]): states[-1][i] = 1
                else: states[-1][i] = 0
                    
            t = tuple(states[-1])
            # check if the state alr exists
            if t in memo: 
                # return the state based on the day at which pattern repeats and the total no. of days
                return states[(n-1)%(day-1)]
            memo[t] = len(states)
            cells = states[-1]
                 
        
        return cells
        