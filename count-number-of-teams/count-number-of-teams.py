class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # for each idx, store how many numbers greater than it and how many numbers less than it
        # in a nested loop, for the third number, get the ans using the prev stored values
        
        n = len(rating)
        
        lesser_count = [0]*n
        greater_count = [0]*n
        
        for i in range(n):
            for j in range(i+1,n):
                # numbers are all unique so these numbers are either greater or lesser than current value
                if rating[i] > rating[j]:
                    lesser_count[i] += 1
                else:
                    greater_count[i] += 1
        
        num_teams = 0
        for i in range(n):
            for j in range(i+1,n):
                if rating[i] > rating[j]:
                    num_teams += lesser_count[j]
                else:
                    num_teams += greater_count[j]
        
        return num_teams