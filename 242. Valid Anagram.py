from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        counter1 = Counter()
        counter2 = Counter()

        counter1.update(s)
        counter2.update(t)

        return counter1 == counter2



