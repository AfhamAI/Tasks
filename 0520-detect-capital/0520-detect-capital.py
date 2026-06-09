class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        else:
            return False




        # c = 0
        # d = 1
        # if len(word) == 1:
        #     return True
        # if word == word.lower():
        #     return True
        # for i in range(1,len(word)):
        #     if word[0] == word[0].upper() and word[i] == word[i].lower():
        #         d += 1
        #     else:
        #         break

        # for i in word:
        #     if i == i.upper():
        #         c += 1

        # if c == len(word):
        #     return True
        # elif d == len(word):
        #     return True 
        # else:
        #     return False


            