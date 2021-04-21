class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        s = word
        while (s in sequence):
            s+=word
            ans+=1
        return ans