class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        new1 = ''.join(word1)
        new2 = ''.join(word2)

        if new1 == new2:        
            return True
        else: 
            return False        