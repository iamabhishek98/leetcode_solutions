from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        # recursive fn
        def kSum(index,k,target):
            kList = None
            if k == 2: 
                # this creates the initial list and the following k values get appended to this list
                return twoSum(index,target)
            else:
                kList = []
                i = index
                while i < len(nums)-k+1:
                    
                    temp = kSum(i+1,k-1,target-nums[i])
                    
                    # temp not None means that particular combination added up to target 
                    # so it can be appended to the ans
                    if temp is not None:
                        for l in temp:
                            l.insert(0,nums[i])
                            kList.append(l)
                    
                    # because it was already considered for the combination
                    i+=1
                    
                    # to get rid of duplicates
                    while i < len(nums)-k+1 and nums[i] == nums[i-1]: i+=1
            
            return kList             
            
        def twoSum(index,target):
            twoSumList = []
            left = index
            right = len(nums)-1
            
            while left<right:
                s = nums[left]+nums[right]
                if s<target: left+=1
                elif s>target: right-=1
                else:
                    twoSumList.append([nums[left],nums[right]])
                    
                    # because both were already used in the combination
                    left+=1
                    right-=1
                    
                    # to get rid of duplicates
                    while left<right and left != index and nums[left] == nums[left-1]: left+=1
                    while left<right and right != len(nums)-1 and nums[right] == nums[right+1]: right-=1      
            
            return twoSumList
                
        return kSum(0,3,0)