class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        start = 0
        end = len(arr)-1
 
        if x < arr[start]:
            return arr[:k]
        elif x > arr[end]:
            return arr[-k:]

        closest_val = sys.maxint
        closest_target = -1
        while start<=end:    
            mid = start+(end-start)//2
            
            if (abs(x-arr[mid]) < abs(x-closest_val)) or ((abs(x-closest_val) == abs(x-arr[mid])) and arr[mid]<closest_val):
                closest_target = mid
                closest_val = arr[mid]
            
            if arr[mid]==x: 
                break
            elif arr[mid]>x:
                end = mid-1
            elif arr[mid]<x:
                start = mid+1
        
        
        ans = [closest_val]
        i = j = closest_target
        
        while len(ans)<k:
            if i-1 >= 0 and j+1<len(arr):
                if abs(arr[i-1]-x)<=abs(arr[j+1]-x):
                    ans.insert(0,arr[i-1])
                    i-=1
                else:
                    ans.append(arr[j+1])
                    j+=1
            elif i-1 >= 0:
                ans.insert(0,arr[i-1])
                i-=1
            elif j+1<len(arr):
                ans.append(arr[j+1])
                j+=1
        
        return ans