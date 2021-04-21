class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        arr = [0]*num_people
        i = 0
        while(candies):
            j = i%num_people
            curr = 0
            if (candies >= i+1): 
                curr = (i+1)
            else: 
                curr = candies
            arr[j]+=curr
            candies-=curr
            i+=1
        return arr