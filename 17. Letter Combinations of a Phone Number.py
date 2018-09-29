# coding=utf-8

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        keymap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        results = [""]
        for d in digits:
            values = keymap[d]
            res = []
            for r in results:
                for v in values:
                    res.append(r + v)
            results = res
        if "" in results:
            results.remove("")
        return results


if __name__ == '__main__':
    s = Solution()
    r = s.letterCombinations("234")
    print(r)
