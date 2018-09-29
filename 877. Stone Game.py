class Solution:

    def whoWins(self, Alex, Lee, piles):

        if piles == []:
            if Alex > Lee:
                return True
            return False
        else:
            return self.whoWins(Alex + piles[0], Lee + piles[-1], piles[1:-1]) or self.whoWins(Alex + piles[-1],
                                                                                               Lee + piles[0],
                                                                                               piles[1:-1])

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        return self.whoWins(0, 0, piles)


if __name__ == '__main__':
    r = Solution().stoneGame([6, 9, 4, 3, 9, 8])
    print(r)
