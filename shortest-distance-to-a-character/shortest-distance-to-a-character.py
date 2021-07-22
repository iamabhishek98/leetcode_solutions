class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        # https://www.youtube.com/watch?v=YMKpDBmDJQE&ab_channel=NickWhite
        
        distances = []
        last_c = len(s)
        # loop through from left to right and calc distance from last occurence of c
        for i in range(len(s)):
            if s[i] != c:
                last_c = min(last_c+1,len(s))
            else:
                last_c = 0
            distances.append(last_c)
        
        # loop through from right to left and calc distance from last occurence of c
        # then choose the minimum distance between the previous set of distances and the last_c
        last_c = len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] != c:
                last_c = min(last_c+1,len(s))
            else:
                last_c = 0
            distances[i] = min(distances[i],last_c)
                
        
        return distances