class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original *= 2
        return original



        # while original in nums:
        #     for i in nums:
        #         if i == original:
        #             original = original*2
        #             break
        #     else:
        #         return original
        # return original
        

        
            
        