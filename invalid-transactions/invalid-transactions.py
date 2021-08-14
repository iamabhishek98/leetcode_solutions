class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        t_map = {}
        invalid = []
        
        for i,t in enumerate(transactions):
            name,time,amount,city = t.split(",")
            if name in t_map: t_map[name].append((time,amount,city))
            else: t_map[name] = [(time,amount,city)]
             
        for name, trans in t_map.items():
            if len(trans) == 1 and int(trans[0][1]) > 1000:
                invalid.append(name+","+','.join(trans[0]))
                continue
                
            for i in range(0,len(trans)):
                for j in range(0,len(trans)):
                    if i == j: continue
                        
                    if (trans[i][2] != trans[j][2] and abs(int(trans[i][0])-int(trans[j][0])) <= 60) or int(trans[i][1]) > 1000:
                        invalid.append(name+","+','.join(trans[i]))
                        break
                    
        
        return invalid