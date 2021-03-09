# -*- coding: utf-8 -*-
# @File    : 5495. 圆形赛道上经过次数最多的扇区.py
# @Time    : 2020/8/23 10:32
# @Author  : libowei

from collections import Counter

class Solution(object):
  def mostVisited(self, n, rounds):
    """
    :type n: int
    :type rounds: List[int]
    :rtype: List[int]
    """

    # 找到第一个递增区间 和 最后一个递增区间

    dizeng1 = []
    dizeng_last = []

    for i in range(len(rounds)):
      if i+1<len(rounds) and rounds[i]<rounds[i+1]:
        dizeng1.append(rounds[i])
      else:
        dizeng1.append(rounds[i])
        break

    print(dizeng1)

    nixu = rounds[::-1]
    for i in range(len(rounds)):
      if i+1 < len(rounds) and nixu[i]>nixu[i+1]:
        dizeng_last.append(nixu[i])
      else:
        dizeng_last.append(nixu[i])
        break

    print(dizeng_last[::-1])

    if dizeng1 == dizeng_last[::-1]:
      return [i for i in range(dizeng1[0],dizeng1[-1]+1)]
    else:


      dizeng_last = dizeng_last[::-1]

      counter = Counter()
      counter.update([i for i in range(dizeng1[0],n+1)])
      counter.update([i for i in range(1, dizeng_last[-1] + 1)])

      print(counter.most_common())

      max_value = counter.most_common(1)[0][1]

      result = []

      for i in range(1,n+1):
        if counter.get(i,-1) == max_value:
          result.append(i)

      return result



if __name__ == '__main__':
  a =  Solution().mostVisited(3,[2, 1, 2, 1, 3, 2, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 3, 2, 3, 2, 1, 2, 3, 1, 3])
  print(a)

