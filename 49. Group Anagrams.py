class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dicts={}
        for word in strs:
            chars = [c for c in word]
            chars.sort()
            key = "".join(chars)
            if key not in dicts:
                dicts[key]=[]
            dicts[key].append(word)


        return list(dicts.values())


if __name__ == '__main__':

    s = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(s)