class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []

        for i, char in enumerate(s):
            if not stack:
                stack.append(i)

            else:
                if char == "(":
                    stack.append(i)
                else:
                    if s[stack[-1]] == "(":
                        stack.pop(-1)
                    else:
                        stack.append(i)

        stack.insert(0,-1)
        stack.append(len(s))

        return max([stack[i + 1] - stack[i] - 1 for i in range(len(stack) - 1)])


if __name__ == '__main__':
    r = Solution().longestValidParentheses("(((((()))")
    print(r)
