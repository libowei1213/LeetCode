# -*- coding: utf-8 -*-
# @File    : 1540. K 次操作转变字符串.py
# @Time    : 2020/8/22 18:26
# @Author  : libowei




from collections import defaultdict

class Solution(object):
  def canConvertString(self, s, t, k):
    """
    :type s: str
    :type t: str
    :type k: int
    :rtype: bool
    """
    if len(s)!=len(t):
      return False
    if s == t:
      return True

    counts = defaultdict(int)

    for i in range(len(s)):
      time = (ord(t[i])-ord(s[i]))%26
      if time>0:
        counts[time]+=1

    print(counts)

    min_count = max(counts.keys())
    if min_count>k:
      return False
    for key,value in counts.items():
      if value>1:
        min_count = key+ 26*(value-1)
        if min_count>k:
          return False

    return True


if __name__ == '__main__':
  a = Solution().canConvertString("jicfxaa","ocxltbp",15)
  print(a)
