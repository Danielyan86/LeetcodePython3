class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves_dic = collections.Counter(moves)
        return moves_dic["U"] == moves_dic["D"] and moves_dic["L"] == moves_dic["R"]
