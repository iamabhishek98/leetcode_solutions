class Solution:
    def totalMoney(self, n: int) -> int:
        div = floor(n/7)
        rem = n%7
        
        total = 0
        if (div == 1): total+=28
        elif (div>1):
            i = 0
            while (i < div):
                total+=(28+7*i)
                i+=1
        
        for j in range(1,rem+1):
            total+=(div+j)
        return total