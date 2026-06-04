class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        hashMap = {}

        for i in range(0,n):
            remaining = target - nums[i]

            if remaining in hashMap:
                return [hashMap[remaining] , i]
            else:
                hashMap[nums[i]] = i