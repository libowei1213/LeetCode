class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        result = []

        for word in words:
            table1 = {}
            table2 = {}
            for i, char in enumerate(word):

                if char not in table1:
                    table1[char] = pattern[i]
                if pattern[i] not in table2:
                    table2[pattern[i]] = char

                if table1[char] != pattern[i] or table2[pattern[i]] != char:
                    break

            else:
                result.append(word)

        return result


if __name__ == '__main__':
    r = Solution().findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
    print(r)
