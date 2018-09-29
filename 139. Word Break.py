def search(s, wordDict, dict):
    if s in dict:
        return dict[s]

    if not s:
        return []

    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)

        else:
            rest = search(s[len(word):], wordDict, dict)
            for item in rest:
                res.append("%s %s" % (word, item))
    dict[s] = res
    return res


class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ans = search(s, wordDict, {})
        return ans


if __name__ == '__main__':
    r = Solution().wordBreak("aaaaaaa",
                             ["aaaa", "aa", "a"])
    print(r)
