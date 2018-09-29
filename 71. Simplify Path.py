class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        paths = path.split("/")

        simple = []

        for folder in paths:
            if folder == '':
                continue
            elif folder == '.':
                continue
            elif folder == "..":
                # 注意"/.."的情况
                if simple!=[]:
                    simple.pop()
            else:
                simple.append(folder)

        return "/" + "/".join(simple)


if __name__ == '__main__':
    r = Solution().simplifyPath("/home/")
    print(r)