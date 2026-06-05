class Solution(object):
    def numberGame(self, nums):
        arr = []
        while len(nums) != 0:
            alice = nums.pop(nums.index(min(nums)))
            bob = nums.pop(nums.index(min(nums)))

            arr.append(bob)
            arr.append(alice)
        return arr
