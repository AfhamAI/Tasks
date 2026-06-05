class Solution(object):
    def maxDepth(self, s):
        count = 0
        depth = 0

        for i in s:
            if i == "(":
                count += 1
                if count > depth:
                    depth = count
            elif i == ")":
                count -= 1
        return depth

        