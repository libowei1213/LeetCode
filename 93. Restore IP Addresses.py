class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.dfs(s, ans, 0, "")
        return ans

    def dfs(self, str, ans, index, ip):
        if index == 4 and str == "":
            ans.append(ip)
            return
        if len(str) > (4 - index) * 3 or len(str) < 4 - index:
            return

        size = min(len(str) + 1, 4)
        for i in range(1, size):
            if str[0] == '0' and len(str[0:i]) > 1:
                continue
            num = int(str[0:i])
            if num > 255:
                continue
            _ip = ip + str[0:i]
            if index < 3:
                _ip += "."
            self.dfs(str[i:], ans, index + 1, _ip)


if __name__ == '__main__':
    r = Solution().restoreIpAddresses("000256")
    print(r)
