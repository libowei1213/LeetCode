# -*- coding: utf-8 -*-
# @File    : 5496. 你可以获得的最大硬币数目.py
# @Time    : 2020/8/23 10:59
# @Author  : libowei


class Solution(object):
  def maxCoins(self, piles):
    """
    :type piles: List[int]
    :rtype: int
    """

    piles = sorted(piles)

    if len(piles)==3:
      return piles[1]

    start = len(piles)//3

    result = 0
    piles = piles[start:]

    for i in range(len(piles)):
      if i%2==0:
        result += piles[i]

    return result


if __name__ == '__main__':
    a = Solution().maxCoins([2,4,1,2,7,8])
    print(a)