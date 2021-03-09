# -*- coding: utf-8 -*-
# @File    : 1541. 平衡括号字符串的最少插入次数.py
# @Time    : 2020/8/22 20:28
# @Author  : libowei

import math

class Solution(object):
  def minInsertions(self, s):
    """
    :type s: str
    :rtype: int
    """

    count = 0
    left = 0

    i=0
    while i<len(s):
      if s[i]=="(":
        left+=1
      else:
        if i+1<len(s) and s[i+1]==")":
          i+=1
        else:
          count+=1
        if left>0:
          left-=1
        else:
          count+=1
      i+=1

    count+=left*2


    return count




if __name__ == '__main__':
    a = Solution().minInsertions("(()))(()))()())))")
    print(a)

