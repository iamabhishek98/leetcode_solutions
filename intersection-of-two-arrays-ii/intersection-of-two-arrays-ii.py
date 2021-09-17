from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Method 1
        
        c1 = Counter(nums1)
        
        intersection = []
        
        for ele in nums2:
            if c1.get(ele, 0) > 0:
                c1[ele] -= 1
                intersection.append(ele)
        
        return intersection
                
#         # Method 2
#         c1 = Counter(nums1)
#         c2 = Counter(nums2)
        
#         intersection = []
        
#         for k1 in c1:
#             intersection.extend(min(c1[k1],c2.get(k1,0))*[k1])
        
#         return intersection


#         # Method 3
    
#         s1 = set()
#         s2 = set()
#         m1 = {}
#         m2 = {}
#         for i in nums1:
#             s1.add(i)
#             if (i in m1): m1[i]+=1
#             else: m1[i]=1
#         for i in nums2:
#             s2.add(i)
#             if (i in m2): m2[i]+=1
#             else: m2[i]=1
#         inter = (list(s1 & s2))
#         ans = []
#         for i in inter:
#             ans.extend([i]*min(m1[i],m2[i]))
#         return ans