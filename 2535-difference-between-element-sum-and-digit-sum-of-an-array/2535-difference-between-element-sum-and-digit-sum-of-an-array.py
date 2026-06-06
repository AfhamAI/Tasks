class Solution(object):
    def differenceOfSum(self, nums):
        digits = ""
        elementSum = sum(nums)
        
        for i in nums:
            digits += str(i)
        digitsSum = 0
        for i in digits:
            digitsSum += int(i)
        
        result = elementSum - digitsSum
        return abs(result)
