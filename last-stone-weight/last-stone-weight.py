import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # https://www.youtube.com/watch?v=fBPS7PtPtaE&ab_channel=KevinNaughtonJr.
        # idea is to keep track of maximum and 2nd maximum in the stones
        max_heap = []
        heapq.heapify(max_heap)
        
        for stone in stones:
            heapq.heappush(max_heap, -1*stone)
        
        while len(max_heap)>1:
            max_stone = -1*heapq.heappop(max_heap)
            max_stone_2 = -1*heapq.heappop(max_heap)
            
            # if they are equal, they are not added back to the max heap because they are "destroyed"
            
            # if they are not equal, the difference is added back to he max heap
            if max_stone != max_stone_2:
                heapq.heappush(max_heap,-1*(max_stone-max_stone_2))
                
        if not max_heap: return 0
        # only 1 item left
        return -1*max_heap[0]