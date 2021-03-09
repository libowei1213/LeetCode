# -*- coding: utf-8 -*-
# @File    : 1539. 第 k 个缺失的正整数.py
# @Time    : 2020/8/22 18:11
# @Author  : libowei


class Solution(object):
  def findKthPositive(self, arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """

    index = 0
    count = 0
    for i in range(1,1000000):
      if index>=len(arr) or i !=arr[index]:
        count+=1
      else:
        index+=1

      if count==k:
        return i




if __name__ == '__main__':
    a = Solution().findKthPositive( [1,2,3,4],2)
    print(a)