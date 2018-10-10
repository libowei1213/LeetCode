from collections import Counter


class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """

        counterB = Counter()
        for i, word in enumerate(B):
            counter = Counter(word)
            for x in counter:
                counterB[x] = max(counterB[x], counter[x])

        ans = []

        for word in A:
            counterA = Counter(word)

            for key in counterB:
                if counterA[key] < counterB[key]:
                    break
            else:
                ans.append(word)

        return ans


if __name__ == '__main__':
    r = Solution().wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"])
    print(r)
