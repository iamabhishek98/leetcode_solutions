from collections import Counter

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # https://medium.com/@crazcuber/amazon-interview-question-partition-labels-aebe54d24d9e
        # algo:
        # 1. Have a frequency table/array(called right) of the whole string.
        # 2. Iterate over string from the left and storing all character we have seen in a set and update the frequency table of the right.
        # 3. Whenever we have a character turn 0 in the table(the character is only in the left) we remove it from the seen set as it is only in the left now.
        # 4. If seen is empty that means that everything on the left is only in that partition hence we can add it to the ans array reset our count
        
        right = Counter(s)
        seen = set()
        count = 0
        ans = []
        
        for i, x in enumerate(s):
            count += 1
            seen.add(x)
            right[x] -= 1
            if right[x] == 0:
                seen.remove(x)
                if not seen:
                    ans.append(count)
                    count = 0
                    
        return ans