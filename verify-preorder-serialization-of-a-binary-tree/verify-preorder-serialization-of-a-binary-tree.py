class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """ 
        # for each node we check if we still have empty slots to put it in.
        #     a null node occupies one slot.
        #     a non-null node occupies one slot before he creates two more. the net gain is one.
        
        # before root is inserted there is one slot
        empty_slots = 1
        
        for i in preorder.split(","):
            # that means there is no empty slot to put the current node in
            if empty_slots == 0: return False
            if i == "#": empty_slots -= 1
            else: empty_slots += 1
        
        # there should be no empty slots left once the entire tree has been traversed
        return empty_slots == 0