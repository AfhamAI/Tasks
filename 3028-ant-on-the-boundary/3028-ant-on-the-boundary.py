class Solution(object):
    def returnToBoundaryCount(self, nums):
        
        position = 0
        count = 0
        for i in nums:
            if i > 0:
                position += i
                if position == 0:
                    count += 1
            else:
                position += i
                if position == 0:
                    count += 1

        return count

        