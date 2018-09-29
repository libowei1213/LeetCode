from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        hashtable = defaultdict(int)

        for word in A.split():
            hashtable[word] += 1

        for word in B.split():
            hashtable[word] += 1

        output = [key for key, value in hashtable.items() if value == 1]
        return output