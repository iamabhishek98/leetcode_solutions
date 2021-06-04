class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        ans = []
        prefix = ""
        for c in searchWord:
            prefix += c
            start = 0
            end = len(products)-1
            found_index = -1
            while start <= end:
                mid = start+(end-start)/2
                curr = products[mid][0:len(prefix)]
                if curr>prefix:
                    end = mid-1
                elif curr<prefix:
                    start = mid+1
                else:
                    found_index = mid
                    break
            arr = []
            if found_index != -1:
                while found_index-1 >= 0 and products[found_index-1][0:len(prefix)] == prefix:
                    found_index -= 1
                while found_index < len(products) and len(arr)<3 and products[found_index][0:len(prefix)] == prefix:
                    arr.append(products[found_index])
                    found_index+=1
            ans.append(arr)
        return ans