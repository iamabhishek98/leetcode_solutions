class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        i = 0
        maxUnits = 0
        while truckSize and i<len(boxTypes):
            currCount = boxTypes[i][0]
            
            if boxTypes[i][0]>truckSize:
                currCount = truckSize
            
            maxUnits+=currCount*boxTypes[i][1]
            truckSize-=currCount
            i+=1
            
        return maxUnits