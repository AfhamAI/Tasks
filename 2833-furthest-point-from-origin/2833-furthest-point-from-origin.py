class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        r = moves.count("R")
        l = moves.count("L")

        if r > l:
            moves = moves.replace("_","R")
        else:
            moves = moves.replace("_","L")

        pos = 0

        for i in moves:
            if i == "L":
                pos -= 1
            elif i == "R":
                pos += 1
            else:
                pos += 1

        return (abs(pos))

