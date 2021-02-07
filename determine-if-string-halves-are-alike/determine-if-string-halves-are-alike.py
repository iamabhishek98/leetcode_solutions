def countVowels(s):
    c = 0
    for i in s:
        if (i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']): c+=1
    return c

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = floor(len(s)/2)
        return countVowels(s[0:n]) == countVowels(s[n:])