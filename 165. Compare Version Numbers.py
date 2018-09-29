class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = list(map(lambda x: int(x), version1.split(".")))
        version2 = list(map(lambda x: int(x), version2.split(".")))

        size1 = len(version1)
        size2 = len(version2)

        if size1 > size2:
            version2 += [0] * (size1 - size2)
        if size1 < size2:
            version1 += [0] * (size2 - size1)

        for i in range(len(version1)):
            if version1[i] > version2[i]:
                return 1
            if version1[i] < version2[i]:
                return -1
        return 0


if __name__ == '__main__':
    r = Solution().compareVersion("1", "1.1")
    print(r)
