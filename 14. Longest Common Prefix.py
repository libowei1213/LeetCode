class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""

        num = len(strs)

        if num == 1:
            return strs[0]

        if strs == []:
            return ""

        str1 = strs[0]

        if str1 == "":
            return ""

        try:

            for i in range(len(str1)):
                for j in range(1, num):
                    if str1[i] != strs[j][i]:
                        return prefix
                prefix += str1[i]

        except IndexError:
            pass

        return prefix