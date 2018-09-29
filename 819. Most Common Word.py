import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        words = re.sub(r"[!\?',;\.]", " ", paragraph).split()
        counter = Counter()
        for word in words:
            word = word.lower()
            if word not in banned:
                counter.update([word])
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    r = Solution().mostCommonWord("Bob!?/ hit a ball, the hit BALL flew far after it was hit.", [])
