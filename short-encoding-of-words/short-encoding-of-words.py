def check(i,ans):
    s = ans.split("#")
    if i in ans:
        for j in s:
            if len(j)>=len(i) and i == j[-len(i):]: return True
    return False

def count(words):
    ans = words[0]+"#"
    for i in words:
        if check(i,ans): continue
        ans += (i + '#')
    return len(ans)

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words: return 0
        ans1 = count(words)
        ans2 = count(words[::-1])
        return min(ans1,ans2)