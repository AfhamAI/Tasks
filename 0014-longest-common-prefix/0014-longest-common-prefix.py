class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        n = len(strs)
        i = 0
        strs.sort()
        while i<len(strs[0]):
            if strs[0][i] == strs[n-1][i]:
                prefix += strs[0][i]
            else:
                break
            i += 1
        
        return prefix