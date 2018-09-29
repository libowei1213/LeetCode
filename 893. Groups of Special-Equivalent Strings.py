def hash(a, b):
    return "".join(sorted(a)) + "".join(sorted(b))


class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        hashtable = {}

        for string in A:
            a, b = string[::2], string[1::2]
            hashtable[hash(a, b)] = True

        print(hashtable)

        return len(hashtable.keys())


if __name__ == '__main__':
    r = Solution().numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"])
    print(r)
