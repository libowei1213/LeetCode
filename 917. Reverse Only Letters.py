class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """

        letters = [char for char in S if (ord(char) >= ord("a") and ord(char) <= ord("z")) or (
                ord(char) >= ord("A") and ord(char) <= ord("Z"))]
        letters = letters[::-1]

        ans = []

        index = 0
        for i, char in enumerate(S):
            if (ord(char) >= ord("a") and ord(char) <= ord("z")) or (ord(char) >= ord("A") and ord(char) <= ord("Z")):
                ans.append(letters[index])
                index += 1
            else:
                ans.append(S[i])

        return "".join(ans)


if __name__ == '__main__':
    r = Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!")
    print(r)
