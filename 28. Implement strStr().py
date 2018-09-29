class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        needleSize = len(needle)
        haystackSize = len(haystack)

        for index, char in enumerate(haystack):

            if haystackSize - index < needleSize:
                return -1

            flag = True
            j = index
            for i, c in enumerate(needle):
                if haystack[j] != needle[i]:
                    flag = False
                    break
                else:
                    j += 1
            if flag:
                return index

        return -1