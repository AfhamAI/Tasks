class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = []
        for i in range(0,2):
            for j in range(0,n):
                ans.append(nums[j])
        return ans
        